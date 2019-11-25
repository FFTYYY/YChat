import socket

def default_callback(s):
	while True:
		data = input()
		s.sendall(bytes(data , encoding = "utf-8"))


def send(host = "127.0.0.1" , myport = 23333 , tarport = 65432 , callback = default_callback):

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind( (host , myport))
		s.connect( (host, tarport) )

		callback(s)
