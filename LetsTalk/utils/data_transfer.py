
def bytes2str(x):
	return str(x)

def str2bytes(x):
	return bytes(x , encoding = "utf-8")

def bytes2int(x):
	return int.from_bytes(x , byteorder = 'little')

def int2bytes(x , length = 4):
	return x.to_bytes(length , byteorder = 'little')

def int2ip(x):
	a = ((x & 0x000000FF) >> 0)
	b = ((x & 0x0000FF00) >> 8)
	c = ((x & 0x00FF0000) >> 16)
	d = ((x & 0xFF000000) >> 24)
	return "%d.%d.%d.%d" % (d,c,b,a)

def ip2int(x):
	d,c,b,a = [int(w) for w in x.strip().split(".")]
	return (d << 24) | (c << 16) | (b << 8) | (a << 0)

def bytes2ip(x):
	return int2ip(bytes2int(x))
	
def ip2bytes(x):
	return int2bytes(ip2int(x) , 4)
