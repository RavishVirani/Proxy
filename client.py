"""
------------------------------------------------------------------------
Authors: Ravish Virani, Sahil Lalani
Student IDs: 173084290, 183145550
File Name: proxy.py
Updated: 2021-02-10
------------------------------------------------------------------------
Notes:

-This file sends a request to the proxy server which is to be forwarded 
    to the webserver and then receive the messages from the web server
    through the proxy.
------------------------------------------------------------------------
"""

# Import socket module
from socket import * 
import sys # In order to terminate the program

# Assign a port number
server_host = "localhost"
servername = sys.argv[1]
serverPort = 8888

if len(sys.argv) < 1:
    print('No Website has been Specified.')
    print('Terminating the request!!!')
    sys.exit(2)

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)
try: 
    clientSocket.connect((server_host, serverPort))
    print("Connected successfully to: ", (server_host, serverPort))
except Exception as e:
    print("Connection error! Unable to connect to: " ,(server_host, serverPort))

request =  f"GET {servername}/ HTTP/1.1\r\n\r\n"
try:
    clientSocket.sendall(request.encode())
    print("Message sent successfully!")
except Exception as f:
    print("Failed to send message!")
    sys.exit(2)
    
recv_mess = clientSocket.recv(2500)
print('From server: \n', recv_mess.decode())
clientSocket.close()
