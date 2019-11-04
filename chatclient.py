from socket import *
serverName = "flip2.engr.oregonstate.edu"
serverPort = 30099
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True:
	sentence = input("Message: ")
	clientSocket.send(sentence.encode())
	if(sentence == "\quit"):
		clientSocket.close()
		exit()
	sentence = clientSocket.recv(1024)
	if(sentence == "\quit"):
		clientSocket.close()
		exit()
	print("From Server: ", sentence.decode())
