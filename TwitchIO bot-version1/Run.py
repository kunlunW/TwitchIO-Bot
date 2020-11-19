import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
        readbuffer = readbuffer + (s.recv(1024).decode("utf-8"))
        temp = readbuffer.split("\n")
        readbuffer = temp.pop()
		
        for line in temp:
            print(line)
            if "PING" in line:
                s.send(bytes(line.replace("PING","PONG"),'UTF-8'))
#                s.send(line.replace("PING", "PONG"))
                break
            user = getUser(line)
            message = getMessage(line)
            print (user + " typed :" + message)
            if "You Rock" in message:
                sendMessage(s, "No, you suck!")
            if "How to move microscope" in message:
                sendMessage(s,"type command: !moveup, !movedown, !moveleft, !moveright")
            if "microscope" in message:
                sendMessage(s,"To move stage, type command: !moveup, !movedown, !moveleft, !moveright")
            if "Microscope" in message:
                sendMessage(s,"To move stage, type command: !moveup, !movedown, !moveleft, !moveright")
            if "?" in message:
                sendMessage(s,"Hello! :) This is ScopyBot! How can I help you? Below are several things that I can help you 1.How to move microscope? 2. How to zoom in/zoom out? 3.Learn more about me B)")
                break
			
