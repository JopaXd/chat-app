import socket
import threading
import logging
import json

#TODO: Make the closing of the server much easier when running from cmd.

#Thought about the commands system thing i did down there.
#When one of tehse commands is executed just make sure that the client doesn't display anything. Simple as that.

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

	def _client_handler(self, connection):
		#The first data being sent is gonna give us the information about the user.
		#After that we're expecting only messages to be sent.
		client = Client(connection)
		self.clients.append(client)
		user_data_acquired = False
		while True:
			if not user_data_acquired:
				#User data contains just the username, so its just one string.
				user_data = client.connection.recv(self.recv_data)
				client.username = user_data.decode(self.encoding_format)
				user_data_acquired = True
			else:
				#Got the data about the user needed now wait for messages.
				#Get the amount of data that is being expected.
				amt_data = int(client.connection.recv(self.recv_data).decode(self.encoding_format))
				logging.info(f"Recieved: {amt_data} bytes of data!")
				#Get the actual data.
				data = client.connection.recv(amt_data)
				if not data:
					pass
				if (text := data.decode(self.encoding_format)) == "!disconnect":
					client.connection.close()
					self.clients.remove(client)
					logging.info(f"Client disconnected!")
					break
				elif text == "!users":
					users = json.dumps({"users": [client.username for client in self.clients]}).encode(self.encoding_format)
					users_data_len = len(users)
					#Send the ammount of data first
					client.connection.sendall(str(users_data_len).encode(self.encoding_format))
					#Then send the actual data.
					client.connection.sendall(users)
					pass
				else:
					message = f"{client.username}: {text}".encode(self.encoding_format)
					logging.info(text)
					self.broadcast_message(message)

	def broadcast_message(self, msg):
		for client in self.clients:
			#Send the amount of data being sent
			msg_size = len(msg)
			#First send the message size
			client.connection.sendall(str(msg_size).encode(self.encoding_format))
			#Then send the actual data.
			client.connection.sendall(msg)

	def start_server(self):
		self.ss.bind((self.ip_address, self.port))
		logging.info("Server online!")
		logging.info(f"Address: {self.ip_address}")
		logging.info(f"Port: {self.port}")
		while True:
			self.ss.listen()
			Client, address = self.ss.accept()
			logging.info('Client connected: ' + address[0] + ':' + str(address[1]))
			new_thread = threading.Thread(target=self._client_handler, args=(Client,))
			new_thread.start()
			self.thread_count +=1

if __name__ == "__main__":
	logging_format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%H:%M:%S")
	chatServer = Server()
	chatServer.start_server()