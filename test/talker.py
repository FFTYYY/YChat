from LetsTalk.talk_sys import ListenServer , SendServer
import random

def main():

	my_snd_port = random.randint(20000 , 60000)
	my_lis_port = int( input ("my listen port: ") )
	
	lis_server = ListenServer(port = my_lis_port)
	lis_server.start()

	tarport 	= int( input ("the listen port you want to connect to: ") )

	print ("[  my send   port is %d  ]" % my_snd_port)
	print ("[  my listen port is %d  ]" % my_lis_port)
	print ("[ tar listen port is %d  ]" % tarport)

	snd_server = SendServer(myport = my_snd_port , tarport = tarport)
	snd_server.start()

if __name__ == "__main__":

	main()
	while True:
		pass
