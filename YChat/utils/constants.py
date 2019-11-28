from .data_transfer import *
import functools
'''
	设计：
		[FLAGS：1 | 源名称长度：4 | 消息上级名称：4 | 消息下级名称：4 | 源名称 | 源数据]
		FLAGS： 
		0：(SPE) 一般消息 / 特殊消息
		1：(STP) 继续消息 / 终止消息
'''

MSG_MAX_LENGTH = 1024
CONTENT_LEN = 250

HEADINFO = [
	["flags" 		, 1 , bytes2int , functools.partial(int2bytes , length = 1)] , 
	["src_ip" 		, 4 , bytes2ip  , ip2bytes ] , 
	["src_port" 	, 4 , bytes2int , int2bytes] , 
]

FLAG_MASK = [
	["SPE" , 1 << 0] , 
	["STP" , 1 << 1] , 
	["ENT" , 1 << 2] ,
	["ADV" , 1 << 3] ,
	["ADD" , 1 << 4] ,
	["QUI" , 1 << 5] ,
]