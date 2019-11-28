from LetsTalk.objects import Room

port = input("输入我的端口（默认为23333）：")
port = 23333 if not port else int(port) 

room = Room(my_ip = "0.0.0.0" , listenport = port).prepare()

try:
	while True: 
		pass
except KeyboardInterrupt:
	room.close()