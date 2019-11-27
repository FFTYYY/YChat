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
	def __init__(self , cont , src_ip , src_port , flags = 0):
		self.cont = cont
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

		self.regularize()
	
	def hasflag(self , flagname):
		return self.flags_dic.get(flagname) or False

	def __str__(self):
		s = "MSG: [ "
		for field_name , field_len , for_func , bak_func in HEADINFO:
			s += repr(self.__dict__[field_name]) + " | "
		s += repr(self.cont) + " ] "
		return s

	def todata(self):

		data = b""
		for field_name , field_len , for_func , bak_func in HEADINFO:
			data += bak_func(self.__dict__[field_name])
		data += bytes(self.cont , encoding = "utf-8")

		return data

	def fromdata(data):
		dic = {}
		reader = DataReader()
		for field_name , field_len , for_func , bak_func in HEADINFO:
			dic[field_name] = for_func(reader(data , field_len))

		dic["cont"] = str(reader(data , -1) , encoding = "utf-8")

		return Message(**dic)


	def regularize(self):
		'''检查消息是否合规，如果不合规，则尝试令其合规，如果无法做到，就抛出异常
		'''
		self.cont = self.cont[:CONTENT_LEN]