import socket
import threading
import logging

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
		user_data_acquired = False
		while True:
			data = connection.recv(2048)
			if not data:
				pass
			if (text := data.decode("utf-8")) == "!disconnect":
				connection.close()
				logging.info(f"Client disconnected!")
				break
			elif text == "!users":
				#return users
				pass
			else:
				broadcast_message(data)

	def broadcast_message(self, msg):
		for client in self.clients:
			client.sendall(data)

	def start_server(self):
		self.ss.bind((self.ip_address, self.port))
		while True:
			self.ss.listen()
			Client, address = self.ss.accept()
			self.clients.append(Client)
			logging.info('Client connected: ' + address[0] + ':' + str(address[1]))
			new_thread = threading.Thread(target=self._client_handler, args=(Client,))
			new_thread.start()
			self.thread_count +=1

if __name__ == "__main__":
	logging_format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%H:%M:%S")
	chatServer = Server()
	chatServer.start_server()