import socket
from .utils.rand_val import rand_port
import copy
import pdb

class SendServer:
	def __init__(self , host = "127.0.0.1"):
		self.host = host

		self.targets = {}

	def add_target(self , tarip = "127.0.0.1" , tarport = 65432):
		#my_port = rand_port()
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect( (tarip, tarport) )		

		self.targets[tarip , tarport] = s

	def remove_target(self , tarip , tarport):
		self.targets[tarip , tarport].close()
		self.targets.pop((tarip , tarport))

	def send(self , data):
		leaved = []
		for tarip , tarport in copy.copy(self.targets):
			if not self.send_to(tarip , tarport , data):
				leaved.append((tarip , tarport))
		return leaved

	def send_to(self , tarip , tarport , data):
		'''return false if connection closed
		'''
		leaved = False

		try:
			self.targets[(tarip , tarport)].sendall(data)
		except ConnectionResetError:
			leaved = True
			
		return not leaved

	def close(self):
		for addr , soc in self.targets.items():
			soc.close()
