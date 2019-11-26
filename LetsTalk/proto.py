from .utils.constants import *

'''
	设计：
		[FLAGS：1 | 源名称长度：4 | 消息上级名称：4 | 消息下级名称：4 | 源名称 | 源数据]
		FLAGS： 
		0：(SPE) 一般消息 / 特殊消息
		1：(STP) 继续消息 / 终止消息
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
	def __init__(self , src_name , msg_cont , src_ip , src_port , flags = 0 , upp_name = 0, low_name = 0):
		self.src_name = src_name
		self.msg_cont = msg_cont
		self.upp_name = upp_name
		self.low_name = low_name
		self.src_ip   = src_ip
		self.src_port = src_port
		
		if isinstance(flags , dict): 
			self.flags_dic = flags
		elif isinstance(flags , list):
			self.flags_dic = {x : True for x in flags}
		elif isinstance(flags , int):
			self.flags_dic = {fname : True if (flags & fmask) != 0 else None for fname , fmask in FLAG_MASK}

		self.flags = 0
		for fname , fmask in FLAG_MASK:
			if self.flags_dic.get(fname):
				self.flags = self.flags | fmask

		self.src_name_len = len(bytes(src_name , encoding = "utf-8"))

	def hasflag(flagname):
		return self.flags_dic.get(flagname) or False

	def __str__(self):
		s = "MSG: [ "
		for field_name , field_len , for_func , bak_func in HEADINFO:
			s += repr(self.__dict__[field_name]) + " | "
		s += repr(self.src_name) + " |"
		s += repr(self.msg_cont) + " ] "
		return s

	def todata(self):

		data = b""
		for field_name , field_len , for_func , bak_func in HEADINFO:
			data += bak_func(self.__dict__[field_name])
		data += bytes(self.src_name , encoding = "utf-8")
		data += bytes(self.msg_cont , encoding = "utf-8")

		return data

	def fromdata(data):
		dic = {}
		reader = DataReader()
		for field_name , field_len , for_func , bak_func in HEADINFO:
			dic[field_name] = for_func(reader(data , field_len))

		dic["src_name"] = str(reader(data , dic['src_name_len']))
		dic["msg_cont"] = str(reader(data , -1))

		dic.pop("src_name_len")

		return Message(**dic)


	def check(self):
		pass