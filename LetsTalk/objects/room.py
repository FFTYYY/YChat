from .base import *

def room_action(obj , msg):

	print (msg.flags_dic , msg.msg_cont)
	if msg.hasflag("SPE"):

		if msg.msg_cont == "ENT":
			'''
				a new member want to enter
			'''
			mem_info = (msg.src_ip , msg.src_port)
			if mem_info in obj.mems:
				raise Exception("multiple connection!")
			obj.connect_member(*mem_info)
			obj.mems.append(mem_info)

			obj.send("oh hello!")

class Room(ConnectObject):
	def __init__(self , my_ip = "127.0.0.1" , name = "" , sendport = None , listenport = 23333):
		super().__init__(my_ip , name , sendport , listenport)

		self.mems = []

	def run(self):
		self.listen_server = ListenServer(host = self.ip , port = self.listenport , callback = self.onget)
		self.listen_server.start()

	def connect_member(self , memb_ip , memb_prot):
		self.send_server = SendServer(host = self.ip , tarip = memb_ip , myport = self.sendport , tarport = memb_prot)
		self.send_server.start()

	def onget(self , data , ip):
		ip , port = ip
		msg = self.from_msg(data)

		room_action(self , msg)
