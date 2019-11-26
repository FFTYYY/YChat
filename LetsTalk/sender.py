import socket

class SendServer:
	def __init__(self , host = "127.0.0.1" , tarip = "127.0.0.1" , myport = 23333 , tarport = 65432):
		self.host 		= host
		self.tarip 		= tarip
		self.myport 	= myport
		self.tarport 	= tarport

	def start(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind( (self.host , self.myport))
		self.socket.connect( (self.tarip, self.tarport) )

	def send(self , data):
		if not hasattr(self , "socket"):
			print ("no socket")
			return	
		self.socket.sendall(data)

	def close(self):
		self.socket.close()
