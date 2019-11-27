from .base import *
from .special_messages import room_special_msgs as specials
from ..utils.hashing import hashing

def room_action(self , msg):

	mem_info = (msg.src_ip , msg.src_port)
	#mem_hash = hashing(*mem_info)

	if msg.hasflag("ENT"):
		'''a new member want to enter
		'''
		if mem_info in self.mem_name:
			raise Exception("multiple connection!")

		self.connect_member(*mem_info)
		self.mem_name[mem_info] = msg.cont

		self.send( specials["advertise"]( self , "%s 加入了聊天室" % msg.cont ) )

		for _ , name in self.mem_name.items():
			self.send( specials["add"]( self , name ) )

	else:
		'''transmit the msg to all members'''
		sender_name = self.mem_name[mem_info]
		self.send( specials["transmit"]( self , msg , sender_name ) )

class Room(ConnectObject):
	def __init__(self , my_ip = "127.0.0.1" , name = "" , listenport = 23333):
		super().__init__(my_ip , name , listenport)

		self.mem_name = {}

	def connect_member(self , memb_ip , memb_prot):
		self.send_server.add_target(tarip = memb_ip , tarport = memb_prot)

	def onget(self , data , ip):
		ip , port = ip
		msg = self.from_msg(data)

		room_action(self , msg)
