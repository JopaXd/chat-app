import socket
import threading
import logging
import json

#TODO: Think about commands !disconnect and !users and if its actually a good idea to do it this way, and is there a better way.
#TODO: Make the closing of the server much easier when running from cmd.

class Client:
	def __init__(self, connection, username=None):
		self.connection	= connection
		self.username = username

class Server:
	def __init__(self, port=7802):
		self.port = port
		self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.thread_count = 0
		self.clients = []

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
				user_data = client.connection.recv(2048)
				client.username = user_data.decode("utf-8")
				user_data_acquired = True
			else:
				#Got the data about the user needed now wait for messages.
				data = client.connection.recv(2048)
				if not data:
					pass
				if (text := data.decode("utf-8")) == "!disconnect":
					client.connection.close()
					logging.info(f"Client disconnected!")
					break
				elif text == "!users":
					#return users
					pass
				else:
					message = str.encode(f"{client.username}: {text}")
					self.broadcast_message(message)

	def broadcast_message(self, msg):
		for client in self.clients:
			client.connection.sendall(msg)

	def start_server(self):
		self.ss.bind((self.ip_address, self.port))
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