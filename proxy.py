"""
------------------------------------------------------------------------
Authors: Ravish Virani, Sahil Lalani
Student IDs: 173084290, 183145550
File Name: proxy.py
Updated: 2021-02-10
------------------------------------------------------------------------
Notes:

-This file starts a proxy server for the mentioned port number.

-This file connects the client to the web server by acting as the 
mediator to send and receive messages.

-To run this file, open a terminal and run file by adding args., like 
so; "python proxy.py localhost 8888"
------------------------------------------------------------------------
"""

#Imports
from socket import *
import sys
import os
import multiprocessing

#Checking the args provided by the user
if len(sys.argv) <=1:
    print('No Port Number or Host Specified.')
    print('Server Shutting Down!')
    sys.exit(2)

#Constants and variables
MAXIMUM_CLIENTS = 10
SERVER_NAME = sys.argv[1]
SERVER_PORT = int(sys.argv[2])
tcpSerSock = socket(AF_INET, SOCK_STREAM)


def tcp_client_handle(tcpCliSock, addr):
    """
    -------------------------------------------------------
    Handeling of each client using the server to connect to
    the web server.
    Use - user = multiprocessing.Process(target=
        tcp_client_handle, args(tcpCliSock, addr))
    -------------------------------------------------------
    Parameters:
        tcpCliSock - Client Socket
        addr - Port Number and Host tuple
    Return:
        NA
    -------------------------------------------------------
    """

    # Strat receiving data from the client
    print('Received a new connection from:', addr)
    message = tcpCliSock.recv(25000).decode()
    
    print(message)

    # Extract the filename from the given message
    fileExist = "false"
    filename = message.split()[1].replace("http://","")
    filename = filename.replace("/","")
    print(filename)

    filetouse = filename + ".cache"


    # Checking if cache file exists

    try:
        print("Checking to see if file exists")
        fh = open(str(filetouse), "rb")
        outputdata = fh.read()
        fileExist = "true"
        
        # ProxyServer finds a cache hit and generates a response message
        print("Cache data for" + filename + " is found.")
        print("Sending response directly from the cache.")
       
        tcpCliSock.sendall(outputdata)
    # Error handling for file not found in cache
    except error as g:

        print(g)
        print("No Cache data found for", filename)

        if fileExist == "false":
            
            print("Connecting to the web server.")
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.","",1)

            try:

                c.connect((hostn, 80))
                # Create a temporary file on this socket and ask port 80
                #for the file requested by the client
                fileobj = c.makefile('rwb', 0)
                fileobj.write(bytes("GET "+"http://" + filename + "/ HTTP/1.1\n\n","utf-8"))

                getdata = f"GET / HTTP/1.1\r\nHost:{filename}\r\n\r\n"

                # Sending message from client to web
                try:
                    print("\nSending GET request from client to the web server")
                    c.sendall(getdata.encode())
                    print("GET request message sent.")
                except:
                    print("\nUnable to send message to Web Server")
                    print("Program terminating with code -1")
                    sys.exit(-1)

                # printing web server message
                try:
                    print("\nGetting the response from the Web Server")
                    data = c.recv(25000)
                    print("Response from the Web Server received")

                except:
                    print("\nUnable to receive response from Web Server")
                    print("Program terminating with code -1")
                    sys.exit(-1)


                # Web Responses
                web_server_response = data.decode()
                http_server_response = web_server_response.split()[1]

                # Make cache if 200 message found
                if http_server_response == "200":
                    print("\nWeb Server responded with 200 OK RESPONSE.")
                    print("Creating a cache file.")
                    tmpFile = open(str(filetouse),'wb')
                    tmpFile.write(data)
                    tmpFile.close()
                else:
                    print("\nWeb Server responded with " + http_server_response + " RESPONSE.")
                
                try:
                    print("\nForwarding the data from the Web Server to the client")
                    tcpCliSock.sendall(data)
                    print(f"Message from the Web Server has been Forwarded to {addr}")
                except:
                    print("\nForwarding the data from the Web Server to the client has failed")
                    print("Terminating the Proxy Server with code -1")
                    sys.exit(-1)

            except error as e :  
                print(e)
                print("Illegal request")

        else:
            # HTTP response message for file not found
            tcpCliSock.send(b"HTTP/1.0 404 Not Found\r\n")
            tcpCliSock.send(b"Content-Type:text/html\r\n")
            tcpCliSock.send(b"\r\n")
            # Fill in start.
            # Fill in end.
            print("\nProgram ending with code -1")
            sys.exit(-1)
    
    # Close the client connection and the exit
    print(f"Connectin with the client {addr} is being Terminated...\n \n")
    tcpCliSock.close()
    exit()


def proxy():
    """
    -------------------------------------------------------
    Uses Multiprocessing to start the server and connect to 
    multiple clients.
    Use - user = multiprocessing.Process(target=
        tcp_client_handle, args(tcpCliSock, addr))
    -------------------------------------------------------
    Parameters:
        tcpCliSock - Client Socket
        addr - Port Number and Host tuple
    Return:
        NA
    ------------------------------------------------------
    """

    # Create a server socket, bind it to a port and start listening
    print('Server ready to serve...')
    tcpSerSock.bind((SERVER_NAME, SERVER_PORT))
    tcpSerSock.listen(MAXIMUM_CLIENTS)

    user_list = []

    print("Server listening to port", SERVER_PORT)

    while True:

        # Starting the proxy broadcast as an infinite loop
        tcpCliSock, addr = tcpSerSock.accept()
        user = multiprocessing.Process(target=tcp_client_handle, args=(tcpCliSock, addr))
        user.start()
        user_list.append(user)


"""
-------------------------------------------------------
Starting the proxy server.
-------------------------------------------------------
"""
if __name__ == "__main__":

    proxy()