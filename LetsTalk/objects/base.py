from ..listener import ListenServer
from ..sender import SendServer
from ..proto import Message
'''
[FLAGS：1 | 源名称长度：4 | 消息上级名称：4 | 消息下级名称：4 | 源名称 | 源数据]
FLAGS： 
0：(SPE) 一般消息 / 特殊消息
1：(STP) 继续消息 / 终止消息
'''

class ConnectObject:
	def __init__(self , my_ip , name , listenport):
		self.listenport = listenport
		self.ip = my_ip
		self.name = name

		self.send_server = SendServer(host = self.ip)


	def from_msg(self , data):
		return Message.fromdata(data)

	def send(self , content , flags = [] , name = None , ip = None):
		msg = Message(
			src_name 	= name or self.name, 
			src_ip 		= ip or self.ip , 
			src_port 	= self.listenport , 
			msg_cont 	= content , 
			flags 		= flags
		)
		self.send_server.send(msg.todata())