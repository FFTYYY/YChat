from .base import *
from .special_messages import memb_special_msgs as specials
from .base import ui_actions

def member_action(self , msg):

	mem_info = (msg.src_ip , msg.src_port)
	mem_hash = hashing(*mem_info)

	if msg.hasflag("ADV"):
		'''an advertisement
		'''
		ui_actions["member_get_advtise"](self , msg.cont)
	if msg.hasflag("ADD"):
		'''tell me members
		'''
		self.room_members.append(msg.cont)
		ui_actions["member_get_mem_name"](self , msg.cont)
	else:
		'''transmitted msg'''

		sender_name = msg.cont.split("\n")[0]
		sender_cont = msg.cont[len(sender_name) + 1 : ]
		ui_actions["member_get_words"](self , sender_name , sender_cont , mem_hash , self.hash)


class Member(ConnectObject):
	def __init__(self , my_ip = "127.0.0.1" , name = "" , listenport = 65432):
		super().__init__(my_ip , name , listenport)

	def connect_room(self , room_ip = "127.0.0.1", room_port = 23333):
		self.room_members = []
		self.send_server.add_target(tarip = room_ip , tarport = room_port)
		self.send( specials["onenter"](self) )

	def say(self , words):
		self.send( specials["say"](self , words) )

	def onget(self , data , ip):
		ip , port = ip
		msg = self.from_msg(data)

		member_action(self , msg)

	def onleave(self , leaved):
		if len(leaved) <= 0:
			return 
		self.close()
		ui_actions["member_server_closed"](self)