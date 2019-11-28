from LetsTalk.objects import Member

port = input("输入我的端口（默认为65432）：")
port = 65432 if not port else int(port) 

name = input("输入我的名称（默认为YYY）：")
name = name or "YYY"

memb = Member(name = name , listenport = port).prepare()

port = input("输入目标的端口（默认为23333）：")
port = 23333 if not port else int(port) 
memb.connect_room(room_port = port)

try:
	while True:
		words = input()
		memb.say(words)
except KeyboardInterrupt:
	memb.close()