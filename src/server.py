import socket
import threading
import logging

class Server:
	def __init__(self, port=7802):
		self.port = port
		self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.thread_count = 0
		self.online = False

	@property
	def ip_address(self):
		#Grabbing the local ip address.
		#In reality you should use the public ip address.
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		ip_addr = s.getsockname()[0]
		s.close()
		return ip_addr

	def _threaded_client_handler(self, connection):
		while True:
			data = connection.recv(2048)
			if not self.online:
				break
			if not data:
				pass
			else:
				connection.sendall(data)

	def start_server(self):
		while True:
			self.online = True
			self.ss.bind((self.ip_address, self.port))
			self.ss.listen()
			Client, address = self.ss.accept()
			logging.info('Connected to: ' + address[0] + ':' + str(address[1]))
			new_thread = threading.Thread(target=self._threaded_client_handler, args=(Client,))
			new_thread.start()
			self.thread_count +=1

if __name__ == "__main__":
	logging_format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%H:%M:%S")
	chatServer = Server()
	print(chatServer.port)
	print(chatServer.ip_address)
	chatServer.start_server()