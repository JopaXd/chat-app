import socket
import threading
import logging 
import json

#TODO: Make the closing of the server much easier when running from cmd.
#TODO:Make some sort of error handler for this.

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

	@property
	def ip_address(self):
		#Grabbing the local ip address.
		#In reality you should use the public ip address.
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		ip_addr = s.getsockname()[0]
		s.close()
		return ip_addr

	def _user_list_handler(self):
		currentClients = len(self.clients)
		while True:
			if (clients := len(self.clients)) != currentClients:
				if clients < currentClients:
					logging.info(f"A user left: {self.clients[-1].username}!")
				elif clients > currentClients:
					logging.info(f"A user joined: {self.clients[-1].username}!")
				if clients != 0:
					currentClients = clients
					data = json.dumps({"data_type": "user_data", "value": [x.username for x in self.clients]}).encode(self.encoding_format)
					self._broadcast_data(data)

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
					logging.info(f"Client disconnected!")
					break
				else:
					message = f"{client.username}: {text}"
					logging.info(f"Broadcasting message: {text}")
					data = json.dumps({"data_type": "message_data", "value": message}).encode(self.encoding_format)
					self._broadcast_data(data)

	def _broadcast_data(self, data):
		for client in self.clients:
			#Send the amount of data being sent
			data_size = len(data)
			#First send the message size
			client.connection.sendall(str(data_size).encode(self.encoding_format))
			#Then send the actual data.
			client.connection.sendall(data)

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
	logging_format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%H:%M:%S")
	chatServer = Server()
	chatServer.start_server()