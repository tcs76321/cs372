Trevor Stahl
stahltr
CS 372 400
Project 1
TCP server client chat


How to Run:
! I was not able to implement a user defined from cmdline handle so,
! and was unable to implement a single word to exit out of both

conect to a flip server directly or through access, for example flip2

I am not sure if you need to but to be safe, please use bash
CMD: bash

Enter dir with my file: chatserve.py

Start server and pass it the port number you want to use like so
Run CMD: 
python3 chatserve.py 30089

and then it will say that it is ready and waiting
displaying just before then hostname it is at and the port number

Open a new putty or something and do a new ssh to flip1

Enter bash again to make sure nothing weird happens

go to where there is a copy of my chatclient.cpp file

Start client
Run CMD: 
gcc -o chatclientCPP chatclient.cpp -lstdc++ -Wall
There should be no warnings or errors
Run CMD: 
chatclientCPP <hostname displayed from starting server> <portnumber>

ie chatclientCPP flip3.engr.oregonstate.edu 30089

you can then send you first message from client

Continue sending messages back and forth between them

When waitin both go to a blank newline and wait

use ctrl C to exit on both, exit might work on client and \quit on server


Citations:
More citations in each file in header comments
W3schools
geeksforgeeks
The class textbook, Kurose
