import socket
import threading

def default_callback(data , ip):
	ip , port = ip
	print (ip , port , ":", data)
				

def listen(host = "127.0.0.1" , port = 65432 , callback = default_callback):

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((host, port))
			s.listen()

			conn_num = 0
			while True:
				conn, addr = s.accept()

				with conn:
					while True:
						data = conn.recv(1024)
						if not data:
							continue
						callback(data , addr)

				if conn_num > 10:
					break

class ListenServer(threading.Thread):
	def __init__(self , host  = "127.0.0.1" , port  = 65432 , callback = default_callback):
		threading.Thread.__init__(self)
		self.setDaemon(True)

		self.host = host
		self.port = port
		self.callback = callback

	def run(self):
		listen(self.host , self.port , self.callback)
