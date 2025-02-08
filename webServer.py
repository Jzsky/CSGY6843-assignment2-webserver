# import socket module
from socket import *
# In order to terminate the program
import sys
from datetime import datetime, timezone, timedelta


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  server_addr = "0.0.0.0"
  serverSocket.bind((server_addr, port))
  
  #Fill in start
  serverSocket.listen(5) 
  #Fill in end
  
  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start -are you accepting connections?     #Fill in end
    # set timeout on the connection
    connectionSocket.settimeout(10)
    print(f"Got a connection from: {addr}")
    
    try:
      message = connectionSocket.recv(1024).decode()#Fill in start -a client is sending you a message   #Fill in end 
      filename = message.split()[1]
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "r")#fill in start #fill in end)
      #fill in end
      header = "HTTP/1.1 200 OK\r\n"
      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
      
      #Content-Type is an example on how to send a header as bytes. There are more!
      content_type = "Content-Type: text/html; charset=UTF-8\r\n"
      content_length = "Content-Length: " + str(f.__sizeof__()) + "\r\n"
      connection= "Connection: close\r\n"
      cache_control = "Cache-Control: no-cache, no-store, must-revalidate\r\n"
      pragma = "Pragma: no-cache\r\n"
      expire = "Expires: 0\r\n"      
      server = "Server: \r\n"
      
      current_datetime = datetime.now(timezone.utc)
      # Format it as an HTTP-compliant date string
      http_date = current_datetime.strftime("%a, %d %b %Y %H:%M:%S GMT")
      date = ("Date: " + http_date + "\r\n")
      
      outputdata = (
            header +
            content_type +
            content_length +
            connection +
            cache_control +
            pragma +
            expire +
            server +
            date   +
            "\r\n"  # End of headers
          )
      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      #Fill in end
        
      for i in f: #for line in file
      #Fill in start - append your html file contents #Fill in end 
        print(i)
        outputdata = outputdata + i
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!
      print(outputdata)
      # Fill in start
      sent = connectionSocket.send(outputdata.encode('utf-8'))
      if sent == 0:
        raise RuntimeError("socket connection broken")

      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      print(e)
      try:
        header = "HTTP/1.1 404 Not Found\r\n"
        #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
        #Fill in start 
                
        #Content-Type is an example on how to send a header as bytes. There are more!
        content_type = "Content-Type: text/html; charset=UTF-8\r\n"
        content_length = "Content-Length: 0\r\n"
        connection= "Connection: close\r\n"
        cache_control = "Cache-Control: no-cache, no-store, must-revalidate\r\n"
        pragma = "Pragma: no-cache\r\n"
        expire = "Expires: 0\r\n"      
        server = "Server: \r\n"
        
        current_datetime = datetime.now(timezone.utc)
        # Format it as an HTTP-compliant date string
        http_date = current_datetime.strftime("%a, %d %b %Y %H:%M:%S GMT")
        date = (http_date+"\r\n")
        
        outputdata = (
            header +
            content_type +
            content_length +
            connection +
            cache_control +
            pragma +
            expire +
            server +
            date   +
            "\r\n"  # End of headers
          )
        sent = connectionSocket.send(outputdata.encode('utf-8'))
        
      except Exception as e:
        print(e)
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
