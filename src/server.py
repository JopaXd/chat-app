import socket
import threading
import logging 
import json

class Client:
	def __init__(self, connection, username=None):
		self.connection	= connection
		self.username = username

class Server:
	def __init__(self, port=7802, recv_data=2048):
		self.port = port
		self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.thread_count = 0
		self.clients = []
		self.recv_data = recv_data
		self.encoding_format = "utf-8"

	#Grabbing the local ip address.
	#In reality you should use the public ip address.
	@property
	def ip_address(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		ip_addr = s.getsockname()[0]
		s.close()
		return ip_addr

	#This handles the list of users/clients
	#If a user/client leaves, this will send an updated list of users to all clients 
	def _user_list_handler(self):
		currentClientsNumber = len(self.clients)
		currentClients = [x for x in self.clients]
		while True:
			if (clients := len(self.clients)) != currentClientsNumber:
				if clients < currentClientsNumber:
					user_who_left = [u.username for u in currentClients if not u in self.clients][0]
					logging.info(f"A user left: {user_who_left}!")
				elif clients > currentClientsNumber:
					logging.info(f"A user joined: {self.clients[-1].username}!")
				if clients != 0:
					data = json.dumps({"data_type": "user_data", "value": [x.username for x in self.clients]}).encode(self.encoding_format)
					self._broadcast_data(data)
				currentClientsNumber = clients
				currentClients = [x for x in self.clients]

	#Main handler for conencted clients.
	#Sends and receives messages from them.
	def _client_handler(self, connection):
		#The first data being sent is gonna give us the information about the user.
		#After that we're expecting only messages to be sent.
		client = Client(connection)
		user_data_acquired = False
		while True:
			if not user_data_acquired:
				#User data contains just the username, so its just one string.
				user_data = client.connection.recv(self.recv_data)
				client.username = user_data.decode(self.encoding_format)
				user_data_acquired = True
				self.clients.append(client)
			else:
				try:
					#Got the data about the user needed now wait for messages.
					#Get the amount of data that is being expected.
					amt_data = int(client.connection.recv(self.recv_data).decode(self.encoding_format))
					logging.info(f"Recieved: {amt_data} bytes of data!")
					#Get the actual data.
					data = client.connection.recv(amt_data)
					if not data:
						pass
					#The disconnect command is subject to delete.
					#Since it won't be needed when i make the client.
					if (text := data.decode(self.encoding_format)) == "!disconnect":
						client.connection.close()
						self.clients.remove(client)
						break
					else:
						message = f"{client.username}: {text}"
						logging.info(f"Broadcasting message: {text}")
						data = json.dumps({"data_type": "message_data", "value": message}).encode(self.encoding_format)
						self._broadcast_data(data)
				except ConnectionResetError:
					try:
						#Just making sure the client is not in the list anymore...
						self.clients.remove(client)
					except:
						pass
					logging.warning("Client disconnected due to ConnectionResetError!")
					break

	#A function to send the data to all connected clients.
	def _broadcast_data(self, data):
		for client in self.clients:
			#Send the amount of data being sent
			data_size = len(data)
			try:
				#First send the message size
				client.connection.sendall(str(data_size).encode(self.encoding_format))
				#Then send the actual data.
				client.connection.sendall(data)
			except:
				#Means the client is not active for whatevr reason, remove it from the list.
				self.client.remove(client)

	def start_server(self):
		self.ss.bind((self.ip_address, self.port))
		userListHandler = threading.Thread(target=self._user_list_handler)
		userListHandler.start()
		logging.info("Server online!")
		logging.info(f"Address: {self.ip_address}")
		logging.info(f"Port: {self.port}")
		while True:
			self.ss.listen()
			Client, address = self.ss.accept()
			logging.info('Client connected: ' + address[0] + ':' + str(address[1]))
			clientHandler = threading.Thread(target=self._client_handler, args=(Client,))
			clientHandler.start()
			self.thread_count +=1

if __name__ == "__main__":
	logging_format = "[%(levelname)s] %(asctime)s: %(message)s"
	logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%H:%M:%S")
	chatServer = Server()
	chatServer.start_server()