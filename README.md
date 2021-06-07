# Proxy Server

######################################################################################################################################
                                                                Authors
######################################################################################################################################
-Ravish Virani: 173084290
-Sahil Lalani: 183145550

######################################################################################################################################
                                                               Environment
######################################################################################################################################
- Python: 3.9
- OS: Windows 10

######################################################################################################################################
                                                               Introduction
######################################################################################################################################
In this assignment we developed a simple proxy proxy which only understands simple HTTPGET-requests, but is able to handle all kinds 
of objects - not just HTML pages, but also images. Generally, when the client makes a request, the request is sent to the web server. 
The proxy server then processes the request and sends back a response message to the requesting client. A proxy server sits between
the client and the web server. Now, both the request message sent by the client and the response message sent by the web server pass 
through the proxy. In other words, the client requests the objects via the proxy. The proxy server will forwardthe client’s request 
to the web server. The web server will then generate a response message and deliver it to the proxy server, which in turn sends it 
to the client. Proxy is used to improve performance and also to improve security.

######################################################################################################################################
                                                              Specifications
######################################################################################################################################
-The proxy server: A simple server which receives the request from the client and forwards it to the server and then receives the 
    message from the server and forwards it back to the client.
- This proxy server can only deal with the HTTP web servers and not the HTTPS servers.
- Error Handeling: The server will send out the error messages if any are encountered in the form of HTTP Responses, like 301, 400, 
    etc.
- Caching: The proxy server will save the website data in a file when a response code of 200 (OK) is received and then forwards this 
    data when the site is accessed in the future.
- Multiprocessing: This is a multi-process server which is able to answer 10 clients at the same time.

######################################################################################################################################
                                                                How to Run
######################################################################################################################################
- Open a terminal and input the hostname, port number as args while launching the proxy.py file. For example, in cmd run it by typing 
    "python proxy.py localhost 8888"
- Next run the client.py file through terminal to get the output.
- To run the client.py, open a terminal and input the website address as the arg while launching the .py file. For example, in cmd
    run it by typing "python client.py www.example.com"
- After running the proxy server you can open the website on a browser instead through the client file by typing the website address
    like this: http://localhost:8888/www.example.com
- This will cache the response in a file in the same directory at first visit.
- If the page is requested again, then the page will be served directly from the local file (cache)

######################################################################################################################################
                                                            Error Handeling
######################################################################################################################################
- The proxy.py file will send any error messages received from the website, like the 400, 404, 301, 302 etc.
- The proxy.py file will also send error exception messages related to file creation, editing, etc.
- The client.py file will send error messages in case connection is not made or message is not sent to the proxy server.

######################################################################################################################################
                                                             Proxy.py Output
######################################################################################################################################

![](Images/1.png)
