from .data_transfer import ip2int

def hashing(ip , port):
	if isinstance(ip , str):
		ip = ip2int(ip)
	return ip * (2 ** 32) + port