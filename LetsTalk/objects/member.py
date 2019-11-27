from .base import *

class Member(ConnectObject):
	def __init__(self , my_ip = "127.0.0.1" , name = "" , listenport = 65432):
		super().__init__(my_ip , name , listenport)

	def run(self):
		pass

	def connect_room(self , room_ip = "127.0.0.1", room_port = 23333):
		self.send_server.add_target(tarip = room_ip , tarport = room_port)
		self.send(
			content = "ENT" , 
			flags = ["SPE"] , 
		)

		self.listen_server = ListenServer(host = self.ip , port = self.listenport)
		self.listen_server.start()		 
