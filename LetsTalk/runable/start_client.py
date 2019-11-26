from LetsTalk.objects import Member

port = input("输入我的端口（默认为65432）：")
port = 65432 if not port else int(port) 

memb = Member(name = "YYY" , listenport = port)
memb.run()

port = input("输入目标的端口（默认为23333）：")
port = 23333 if not port else int(port) 
memb.connect_room()

while True:
	msg = input(">>")
	memb.send(msg)