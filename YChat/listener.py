import socket
import threading
from .proto import Message
from .utils.constants import MSG_MAX_LENGTH

def default_callback(data , ip , who_get = None):
	ip , port = ip
	print (ip , port , ":", Message.fromdata(data))

class ChildListener(threading.Thread):
	def __init__(self , conn , addr , callback , parent):
		threading.Thread.__init__(self)
		self.setDaemon(True)

		self.conn = conn
		self.addr = addr
		self.callback = callback
		self.closed = False
		self.parent = parent

		self.tarip = None
		self.tarport = None #listen port

	def run(self):
		with self.conn:
			while not self.closed:

				try:
					data = self.conn.recv(MSG_MAX_LENGTH)
				except ConnectionResetError:
					if self.parent.unexpect_quit:
						self.parent.unexpect_quit(self.tarip , self.tarport)
					break

				if not data:
					continue
				self.callback(data , self.addr , who_get = self)
		self.close()

	def close(self):
		self.closed = True


class ListenServer(threading.Thread):
	def __init__(self , host  = "127.0.0.1" , port  = 65432 , callback = default_callback):
		threading.Thread.__init__(self)
		self.setDaemon(True)

		self.host = host
		self.port = port
		self.callback = callback

		self.childs = []
		self.closed = False
	
		self.unexpect_quit = None

	def run(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((self.host, self.port))
			s.listen()

			while not self.closed:
				conn, addr = s.accept()

				new_child = ChildListener(conn , addr , self.callback , parent = self)
				new_child.start()
				self.childs.append(new_child)

	def close_one(self , tarip , tarport):
		the_child = None
		for x in self.childs:
			if x.tarip == tarip and x.tarport == tarport:
				the_child = x
				break
		if the_child is None:
			return

		the_child.close()
		self.childs.remove(the_child)

	def close(self):
		for x in self.childs:
			x.close()
		self.closed = True
