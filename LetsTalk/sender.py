import socket
from .utils.rand_val import rand_port

class SendServer:
	def __init__(self , host = "127.0.0.1"):
		self.host = host

		self.targets = {}

	def add_target(self , tarip = "127.0.0.1" , tarport = 65432):
		my_port = rand_port()
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind( (self.host , my_port))
		s.connect( (tarip, tarport) )

		self.targets[tarip , tarport] = s

	def send(self , data):
		for addr , soc in self.targets.items():
			soc.sendall(data)

	def send_to(self , tarip , tarport , data):
		self.targets[(tarip , tarport)].sendall(data)

	def close(self):
		for addr , soc in self.targets.items():
			soc.close()
