from .utils.rand_val import rand_port
from .listener import ListenServer
from .sender import SendServer
from .proto import Message
'''
[FLAGS：1 | 源名称长度：4 | 消息上级名称：4 | 消息下级名称：4 | 源名称 | 源数据]
FLAGS： 
0：(SPE) 一般消息 / 特殊消息
1：(STP) 继续消息 / 终止消息
'''

class ConnectObject:
	def __init__(self , my_ip , name , sendport , listenport ):
		self.sendport = sendport or rand_port()
		self.listenport = listenport
		self.ip = my_ip
		self.name = name

	def form_data(self , content , flags = []):
		msg = Message(src_name = self.name , src_ip = self.ip , src_port = self.listenport , msg_cont = content , flags = flags)
		return msg.todata()

	def from_msg(self , data):
		return Message.fromdata(data)

	def send(self , content , flags = []):
		self.send_server.send(self.form_data(content = content, flags = flags))

class Member(ConnectObject):
	def __init__(self , my_ip = "127.0.0.1" , name = "" , sendport = None , listenport = 65432):
		super().__init__(my_ip , name , sendport , listenport)

	def run(self):
		pass

	def connect_room(self , room_ip = "127.0.0.1", room_port = 23333):
		self.send_server = SendServer(host = self.ip , tarip = room_ip , myport = self.sendport , tarport = room_port)
		self.send_server.start()
		self.send(
			content = "ENT" , 
			flags = ["SPE"] , 
		)

		self.listen_server = ListenServer(host = self.ip , port = self.listenport)
		self.listen_server.start()		 


class Room(ConnectObject):
	def __init__(self , my_ip = "127.0.0.1" , name = "" , sendport = None , listenport = 23333):
		super().__init__(my_ip , name , sendport , listenport)

	def run(self):
		self.listen_server = ListenServer(host = self.ip , port = self.listenport , callback = self.onget)
		self.listen_server.start()

	def connect_member(self , memb_ip , memb_prot):
		self.send_server = SendServer(host = self.ip , tarip = memb_ip , myport = self.sendport , tarport = memb_prot)
		self.send_server.start()

	def onget(self , data , ip):
		ip , port = ip
		msg = self.from_msg(data)

		#self.connect_member(msg.src_ip , msg.src_port)
		print ("from (%s:%d) I got : %s" % (ip,port,str(msg)))

