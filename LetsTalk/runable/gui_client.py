from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
import pdb
import os , sys
from LetsTalk.objects import Member
from LetsTalk.ui.gui_actions import message_box

class Liaison(QObject):

	def __init__(self , parent = None):
		super().__init__(parent = parent)
		self.memb = None
		self._logedin = False

	@pyqtSlot(str,int,str,int,result = bool)
	def login(self,name,port,room_ip,room_port):
		print (repr(name) , repr(port))
		self.memb = Member(name = name , listenport = port).prepare()
		self.memb.connect_room(room_ip = room_ip , room_port = room_port)

		self._logedin = True
		return self._logedin

	@pyqtSlot(result = bool)
	def logedin(self):
		return self._logedin

	@pyqtSlot(str)
	def say(self,words):
		if self.memb is None:
			return
		self.memb.say(words)

	@pyqtSlot(result = str)
	def messages(self):
		return "\n".join(message_box)



path = os.path.relpath( os.path.join(os.path.dirname(__file__) , '../ui/main.qml') , start = ".") #qt quick 只吃相对路径
app = QGuiApplication([])
view = QQuickView()
view.setTitle("LetsTalk")

lia = Liaison()
cont = view.rootContext()
cont.setContextProperty("lia", lia)

view.setSource(QUrl(path))

view.show()
app.exec_()