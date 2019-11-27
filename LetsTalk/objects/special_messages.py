from ..proto import Message

memb_special_msgs = {}
room_special_msgs = {}

def memb_msg_func(name):
	def _memb_msg_func(func):
		memb_special_msgs[name] = func
	return _memb_msg_func

def room_msg_func(name):
	def _room_msg_func(func):
		room_special_msgs[name] = func
	return _room_msg_func

@memb_msg_func("say")
def say(obj , cont = ""):
	return obj.make_msg(
		content = cont , 
	)

@memb_msg_func("onenter")
def onenter(obj):
	return obj.make_msg(
		content = obj.name , 
		flags = ["ENT"] , 
	)


@room_msg_func("transmit")
def transmit(obj , msg , sender_name):
	msg.cont = sender_name + "\n" + msg.cont
	return msg

@room_msg_func("advertise")
def advertise(obj , cont = ""):
	return obj.make_msg(
		content = cont ,  
		flags = ["ADV"] , 
	)

@room_msg_func("add")
def add(obj , name = ""):
	return obj.make_msg(
		content = name ,  
		flags = ["ADD"] , 
	)