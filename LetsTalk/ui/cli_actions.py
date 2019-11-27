
ui_actions = {}

def ui_action(name):
	def _ui_action(func):
		ui_actions[name] = func
	return _ui_action

@ui_action("member_get_advtise")
def member_get_advtise(self , cont):
	print ("【系统提示：%s】" % (cont))

@ui_action("member_get_words")
def member_get_words(self , sender_name , sender_cont):
	print ("%s 说： %s" % (sender_name , sender_cont))

@ui_action("member_get_mem_name")
def member_get_mem_name(self , name):
	print ("【当前聊天室成员：%s】" % name)
