from .listener import  listen , default_callback as default_lis
from .sender import send , default_callback as default_snd
import threading

class ListenServer(threading.Thread):
	def __init__(self , host  = "127.0.0.1" , port  = 65432 , callback = default_lis):
		threading.Thread.__init__(self)
		self.setDaemon(True)

		self.host = host
		self.port = port
		self.callback = callback

	def run(self):
		listen(self.host , self.port , self.callback)

class SendServer(threading.Thread):
	def __init__(self , host  = "127.0.0.1" , myport = 23333 , tarport = 65432 , callback = default_snd):
		threading.Thread.__init__(self)
		self.setDaemon(True)

		self.host 		= host
		self.myport 	= myport
		self.tarport 	= tarport
		self.callback 	= callback

	def run(self):
		send(self.host , self.myport , self.tarport , self.callback)

