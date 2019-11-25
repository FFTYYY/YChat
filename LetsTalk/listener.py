import socket

def default_callback(conn):
	with conn:
		while True:
			data = conn.recv(1024)
			if data:
				print (data)


def listen(host = "127.0.0.1" , port = 65432 , callback = default_callback):

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((host, port))
			s.listen()

			conn_num = 0
			while True:
				conn, addr = s.accept()
				callback(conn)

				if conn_num > 10:
					break

