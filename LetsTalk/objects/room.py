from .base import *
from .special_messages import room_special_msgs as specials
from ..utils.hashing import hashing
from ..utils.logger import Logger

def room_action(self , msg):

	mem_info = (msg.src_ip , msg.src_port)
	#mem_hash = hashing(*mem_info)

	if msg.hasflag("ENT"):
		'''a new member want to enter
		'''
		if mem_info in self.mem_name:
			raise Exception("multiple connection!")

		self.connect_member(*mem_info , mem_name = msg.cont)

		for _ , name in self.mem_name.items():
			self.send( specials["add"]( self , name ) )


	elif msg.hasflag("QUI"):
		if mem_info not in self.mem_name:
			return
		self.remove_member(*mem_info)
		
	else:
		'''transmit the msg to all members'''
		sender_name = self.mem_name[mem_info]
		self.send( specials["transmit"]( self , msg , sender_name ) )


class Room(ConnectObject):
	def __init__(self , my_ip = "127.0.0.1" , name = "" , listenport = 23333):
		super().__init__(my_ip , name , listenport)

		self.mem_name = {}
		self.logger = Logger()

	def connect_member(self , memb_ip , memb_port , mem_name):
		self.send_server.add_target(tarip = memb_ip , tarport = memb_port)
		self.mem_name[(memb_ip , memb_port)] = mem_name
		self.send( specials["advertise"]( self , "%s 加入了聊天室" % mem_name ) )

	def onprepare(self):
		self.listen_server.unexpect_quit = self.remove_member

	def onget(self , data , ip , who_get = None):
		ip , port = ip
		msg = self.from_msg(data)

		who_get.tarip = msg.src_ip
		who_get.tarport = msg.src_port

		room_action(self , msg)

	def remove_member(self , mem_ip , mem_port):
		self.send_server.remove_target(mem_ip , mem_port)
		self.listen_server.close_one(mem_ip , mem_port)
		name = self.mem_name.pop((mem_ip , mem_port))
		self.send( specials["advertise"]( self , "%s 离开了聊天室" % name ) )


	def onleave(self , leaved):
		for x in leaved:
			self.remove_member(*x)
			
