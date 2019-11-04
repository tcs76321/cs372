Trevor Stahl
stahltr
CS 372 400
Project 1
TCP server client chat


How to Run:

conect to a flip server directly or through access, for example flip2

I am not sure if you need to but to be safe, please use bash
CMD: bash

Enter dir with my file: chatserve.py

Start server and pass it the port number you want to use like so
Run CMD: python3 chatserve.py 30089


and then it will say that it is ready and waiting
displaying just before the hostname it is at and the port number

Open a new putty or something and do a new ssh to flip1

go to where there is a copy of my chatclient.c file

Start client
Run CMD: gcc -o chatclient chatclient.c
Run CMD chatclient

It will then ask for 




Citations:
W3schools
geeksforgeeks
The class textbook, Kurose
