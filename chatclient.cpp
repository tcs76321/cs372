/*
 * Trevor Stahl
 * stahltr
 *
 * chatclient.cpp
 *
 * Program description:
 *
 * CS372
 *
 * Last Modified: 11/4/2019
 *
 * Citations: I started out with code from here https://simpledevcode.wordpress.com/2016/06/16/client-server-chat-in-c-using-sockets/
 * and then studied, modified and adapted to the project
 * Also referenced and might have used some of BEEJ's c client.c code
 * I left comments with code that was not working but that I was trying to implement
 */

#include <iostream>
#include <string>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <netdb.h>
#include <sys/uio.h>
#include <sys/time.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <fstream>
using namespace std;
// Did not have time to implement as modular functions
int main(int argc, char *argv[]){
    // Check that the right number of arguements were passed
    // we need 2 things: ip address and port number, in that order
    if(argc != 3){// arg 1 is file to execute I think
        cerr << "Need two arguements of serverName and portnumber of the server to connect to" << endl; 
	exit(0);
    } 
    // get handle
    // string handle;// char handle[20];
    // cin >> handle; // getline(cin, handle);
    //grab the IP address and port number 
    char *serverIp = argv[1];
    int port = atoi(argv[2]); 
    //create a message buffer of size 500 chars
    char msg[500];
    //setup a socket and connection tools 
    struct hostent* host = gethostbyname(serverIp);
    // tools 
    sockaddr_in sendSockAddr;   
    bzero((char*)&sendSockAddr, sizeof(sendSockAddr)); 
    sendSockAddr.sin_family = AF_INET; 
    sendSockAddr.sin_addr.s_addr = inet_addr(inet_ntoa(*(struct in_addr*)*host->h_addr_list));
    sendSockAddr.sin_port = htons(port);
    int clientSd = socket(AF_INET, SOCK_STREAM, 0);
    //try to connect...
    int status = connect(clientSd, (sockaddr*) &sendSockAddr, sizeof(sendSockAddr));
    if(status < 0){
        cout<<"Error connecting to socket!"<<endl; 
    }
    cout << "Connected to the server!" << endl;
    // simple loop for client that sends and then recs
    // when gets exit breaks and then closes and returns out of main
    while(1){

	// was not able to implement user input handle, You here and Client on server, hard coded
	// I tried to expand on this code a lot but everything I did was not working
        cout << "You> ";
        string data;
        getline(cin, data);
        memset(&msg, 0, sizeof(msg));//clear the buffer
        strcpy(msg, data.c_str());
	// char handlemsg[20];
	// strcpy(handlemsg, handle);
	// strcat(handlemsg, msg); tried &msg * msg too
	// was going to change this to be the \\quit it needs to be but could not figure out how in time, alrady one day late
        if(data == "exit")
        {
            send(clientSd, (char*)&msg, strlen(msg), 0);
            break;
        }
	// send message normally
        send(clientSd, (char*)&msg, strlen(msg), 0);//send(clientSd, (char*)&handlemsg, strlen(msg), 0);
	//clear the buffer
        memset(&msg, 0, sizeof(msg));
	// receive message, same ech loop no matter what
        recv(clientSd, (char*)&msg, sizeof(msg), 0);
	// check for exit
        if(!strcmp(msg, "exit"))
        {
            cout << "Server has quit the session" << endl;
            break;// break out if so and close and return 0 out of main
        }
	// otherwise print out message with server handle and then loop back up and send another message
        cout << "Server> " << msg << endl;
    }
    // clean up and return
    close(clientSd);
    cout << "Connection closed" << endl;
    return 0;    
}
