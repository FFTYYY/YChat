import socket
import threading
from .proto import Message


def default_callback(data , ip):
	ip , port = ip
	print (ip , port , ":", Message.fromdata(data))
				

class ChildListener(threading.Thread):
	def __init__(self , conn , addr , callback):
		threading.Thread.__init__(self)
		self.setDaemon(True)

		self.conn = conn
		self.addr = addr
		self.callback = callback

	def run(self):
		with self.conn:
			while True:
				data = self.conn.recv(1024)
				if not data:
					continue
				self.callback(data , self.addr)


class ListenServer(threading.Thread):
	def __init__(self , host  = "127.0.0.1" , port  = 65432 , callback = default_callback):
		threading.Thread.__init__(self)
		self.setDaemon(True)

		self.host = host
		self.port = port
		self.callback = callback

		self.childs = []
	
	def run(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((self.host, self.port))
			s.listen()

			conn_num = 0
			while True:
				conn, addr = s.accept()

				conn_num += 1
				if conn_num > 10:
					break

				new_child = ChildListener(conn , addr , self.callback)
				new_child.start()
				self.childs.append(new_child)

