from .data_transfer import *
import functools

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