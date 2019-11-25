from constants import *

'''
	设计：
	所有机器有两个端口用来通信，一个是监听端口，用来收信息，另一个是发送端口，用来发送信息。
	每条数据：
	[FLAGS：1 | 源ip：4 | 源名称长度：4 | 消息上级名称：4 | 消息下级名称：4 | 源名称 |源数据]
	FLAGS： 
	0：特殊消息 / 一般消息
	1：终止消息 / 继续消息
	其余位留作备用
	每条消息会按时间获得上级名称。在消息拆成多条时，每条子消息按时间获得下级名称。
'''

class DataReader:
	def __init__(self):
		self.reset()
	def reset(self):
		self._now_pos = 0
	def read(self , data , length):
		'''从给定数据中读取特定长度的数据，如果length=-1，则会读取剩下所有数据
		'''
		if length < 0:
			return data[self._now_pos : ]
		self._now_pos += length
		return data[self._now_pos - length : self._now_pos]
	def __call__(self , *pargs , **kwargs):
		return self.read(*pargs , **kwargs)

class Message:
	def __init__(self , data):
		reader = DataReader()
		for field_name , field_len in HEADINFO:
			self.__dict__[field_name] = reader(data , field_len)

		self.check()

		self.SRC_NAME = reader(data , self.SRC_NAME_LEN)
		self.MSG_CONT = reader(data , -1)

	def check(self):
		pass