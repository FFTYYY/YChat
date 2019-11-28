
message_box = []
def mprint (x = ""):
	message_box.append(str(x))

ui_actions = {}

def ui_action(name):
	def _ui_action(func):
		ui_actions[name] = func
	return _ui_action

@ui_action("member_get_advtise")
def member_get_advtise(self , cont):
	mprint ("【系统提示：%s】" % (cont))

@ui_action("member_get_words")
def member_get_words(self , sender_name , sender_cont , mem_hash = 0, self_hash = -1):
	mprint ("%s 说： %s" % (sender_name , sender_cont))

@ui_action("member_get_mem_name")
def member_get_mem_name(self , name):
	mprint ("【当前聊天室成员：%s】" % name)

@ui_action("member_server_closed")
def member_server_closed(self):
	mprint ("【服务关闭了...】")
	exit(0)