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

# Preconditions:
# NONE
# Postconditions:
# Correct number of arguements for rest of program
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

# Preconditions:
# Correct number of arguements
# Postconditions:
# If completes without any errors
# global hostname var with hostname
# global serverSocket is TCP socket, that is binded to serverport passes, and listening for 1 connection
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

# Preconditions:
# connectionSokcet is valid
# there is an open connection
# Postconditions:
# global sentence is what is what was recieved from socket
def recMessage():
	global sentence
	sentence  = connectionSocket.recv(1024).decode()
	res = checkForQuit()
	if(res == "not"):
		print("Client> ", (str(sentence)))
		return "not"
	else:
		return "closed"

# Preconditions:
# connectionSocket is valid
# sentence is global
# Postconditions:
# NONE? I think???
def sendMessage():
	sentence = input("You> ")
	connectionSocket.send(sentence.encode())
	res = checkForQuit()

# Preconditions:
# connectionSocket is valid
# and that it is an open socket connection to close if sentence is \quit
# Postconditions:
# if sentence was \quit connection closed
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

# get the connection started
startUp()

# only want to do this once, originally in recMessage
global connectionSocket
connectionSocket, addr = serverSocket.accept()


while True:
	closer = recMessage()
	if(closer == "closed"):
		continue # continune to allow for another client to connect after this
	sendMessage()

