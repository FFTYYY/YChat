from setuptools import setup , find_packages


with open("README.md", encoding = "utf-8") as f:
	readme = f.read()

reqs = [
	"PyQt5>=5.11.0" , 
]

pkgs = [
	"YChat" , 
	"YChat.objects" , 
	"YChat.ui" , 
	"YChat.utils" , 
	"YChat.runable" , 
]

data_files = [
	"YChat/ui/main.qml" , 
]

setup(
	name					= "YChat",
	version					= "0.1.4",
	url 					= "https://github.com/FFTYYY/YChat",
	description				= "A simple chatroom program.",
	long_description		= readme ,
	install_requires 		= reqs , 
	license					= "MIT License",
	author					= "Yang Yongyi",
	author_email 			= "yongyiyang17@fudan.edu.cn",
	python_requires			= ">=3.6",
	packages				= pkgs,
	entry_points			= {"console_scripts": [
			"YChat-server=YChat.entry:run_server_cli" ,
			"YChat-client=YChat.entry:run_client_gui" ,
		]},
	data_files 				= data_files , 

)
