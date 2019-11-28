from ..listener import ListenServer , default_callback
from ..sender import SendServer
from ..proto import Message
from ..utils.hashing import hashing

from ..ui.gui_actions import ui_actions

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
		self.hash = hashing(my_ip , listenport)

	def prepare(self):		
		self.send_server = SendServer(host = self.ip)

		if hasattr(self , "onget"): callback = self.onget
		else:						callback = default_callback

		self.listen_server = ListenServer(host = self.ip , port = self.listenport , callback = callback)
		self.listen_server.start()
		return self

	def from_msg(self , data):
		return Message.fromdata(data)

	def make_msg(self , content , flags = [] , ip = None):
		return Message(
			src_ip 		= ip or self.ip , 
			src_port 	= self.listenport , 
			cont 		= content , 
			flags 		= flags
		)

	def send(self , content_or_msg , flags = [] , ip = None):

		if isinstance(content_or_msg , Message):
			msg = content_or_msg
		else: msg = self.make_msg(content_or_msg , flags , ip)

		leaved = self.send_server.send(msg.todata())

		if hasattr(self , "onleave"):
			self.onleave(leaved)

	def send_to(self , tarip , tarport , content_or_msg , flags = [] , ip = None):

		if isinstance(content_or_msg , Message):
			msg = content_or_msg
		else: msg = self.make_msg(content_or_msg , flags , ip)
		
		leaved = self.send_server.send_to(tarip , tarport , msg.todata())
		leaved = [(tarip , tarport)] if leaved else []

		if hasattr(self , "onleave"):
			self.onleave(leaved)

	def close(self):
		self.send_server.close()
		self.listen_server.close()
