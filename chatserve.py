# Trevor Stahl
# stahltr
# chatserve.py
# CS_372_400
# Last_Modified: 11/4/2019
# Description: Simple python chat server that uses python3
# Ciations: 
# 1 - Takes code from Kurose Class textbook, modified of course for assignemnt specs
# 2 - geeksforgeeks, heavily modified 

from socket import *
import sys

def checkArguements():
	# check numb of arguements given with running of script
	if len(sys.argv) > 2:
		print("Too many arguements, try again")
		exit()
	elif len(sys.argv) > 1:
		global serverPort
		serverPort = int(sys.argv[1])
	else:
		print("I need a port number to recieve from")
		exit()
	# check for if the arguement is a valid port number
	# only need to check range strings and floating points throw errors when tried to be ran
	if((serverPort > 49151) or (serverPort < 1024)):
		print("I need a port number between and including 1024 and 49151")
		exit()

def startUp():
	global hostname
	hostname = gethostname()
	global serverSocket 
	serverSocket= socket(AF_INET, SOCK_STREAM)
	serverSocket.bind(('',serverPort))
	serverSocket.listen(1)
	print("Serving at: ", hostname)
	print("On port: ", serverPort)
	print("Ready and Waiting...")

def recMessage():
	global sentence
	sentence  = connectionSocket.recv(1024).decode()
	res = checkForQuit()
	if(res == "not"):
		print("", (str(sentence)))
		return "not"
	else:
		return "closed"

def sendMessage():
	sentence = input("Message:")
	connectionSocket.send(sentence.encode())
	res = checkForQuit()

def checkForQuit():
	if(sentence == "\quit"):
		print("Recieved or Sent \quit")
		print("Closing connection and waiting")
		connectionSocket.close()
		return "closed"
	else:
		return "not"
		

# Make sure there are the right number of arguements otherwise exit
# And also then see if the arguement is in the valid range
checkArguements()

startUp()

#only want to do this once
global connectionSocket
connectionSocket, addr = serverSocket.accept()

while True:
	closer = recMessage()
	if(closer == "closed"):
		continue
	sendMessage()

