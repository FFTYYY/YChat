from ..utils.rand_val import rand_port
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