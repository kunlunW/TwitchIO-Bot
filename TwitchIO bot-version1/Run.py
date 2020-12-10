import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

# import the microcontroller class 
from microcontroller import *

#create an instance of microcontroller
testingcontroller = Microcontroller()

s = openSocket()
joinRoom(s)
readbuffer = ""

# This method tests whether a command is a move command
def isMoveCommand (message1):

    print (message1)
    delimeterMessage = message1.split(' ')
    print(delimeterMessage)
    
    if (delimeterMessage[0] == 'move_x'):
        print("recognize move_x successful")
        moveLength = delimeterMessage[1].replace('\r' , '')
        a = moveLength.isdigit()
        print(a)
       
        if (moveLength.isdigit() == True ):
            if (int(moveLength) > 500):
                sendMessage(s,"You cannot move more than 500 pixels")
            print ("recognize number")
            print (type(moveLength))
            moveLength1 = int(moveLength)
            # send signal to microcontroller to move
            # testingcontroller.move_x(moveLength1)
            sendMessage(s,"You moved in x direction for " + moveLength + " pixels")

    if (delimeterMessage[0] == 'move_y'):
        moveLength = delimeterMessage[1].replace('\r' , '')
        a = moveLength.isdigit()
        print (a)
        if (moveLength[1].isdigit() == True ):
            if (int(moveLength) > 500):
                sendMessage(s,"You cannot move more than 500 pixels")
            moveLength1 = int(moveLength)
            # send signal to microcontroller to move
            # testingcontroller.move_y(moveLength1)
            sendMessage(s,"You moved in y direction for " + moveLength + " pixels")

    if (delimeterMessage[0] == 'move_z'):
        moveLength = delimeterMessage[1].replace('\r', '')
        if (moveLength[1].isdigit() == True):
            if (int(moveLength) > 500):
                sendMessage(s,"You cannot move more than 500 pixels")
            moveLength1 = int(moveLength)
            # send signal to microcontroller to move
            # testingcontroller.move_z(moveLength1)
            sendMessage(s,"You moved in z direction for " + moveLength + " pixels")

def controlIllumination (light_message):

    if "light_on" in light_message: 
        sendMessage(s,"You have turned the light on!")
        # testingcontroller.turn_on_illumination()
    if "light_off" in light_message: 
        sendMessage(s,"You have turned the light off!")
        # testingcontroller.turn_off_illumination()


while True:
        # readbuffer to read in user's input 
        readbuffer = readbuffer + (s.recv(1024).decode("utf-8"))
        # setting up the delimiters 
        temp = readbuffer.split("\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            if "PING" in line:
                s.send(bytes(line.replace("PING","PONG"),'UTF-8'))
                break
            user = getUser(line)
            message = getMessage(line)

            print (user + " typed :" + message)
        
            if "move_x" in message or "move_y" in message or "move_z" in message:
                isMoveCommand(message)

            if "illumination" in message: 
                sendMessage(s,"To move turn light on, type command: \"light_on\", To move turn light off, type command: \"light_off\"")
            
            if "light_on" in message or "light_off" in message:
                controlIllumination(message)
                
            if "You Rock" in message:
                sendMessage(s, "No, you suck!")
            if "How to move microscope" in message:
                sendMessage(s,"To move stage for 10 pixels, type command: \"move_x 10\", \"move_y 10\", \"move_y 10\", \"move_y 10\"")
            if "microscope" in message:
                sendMessage(s,"To move stage for 10 pixels, type command: \"move_x 10\", \"move_y 10\", \"move_y 10\", \"move_y 10\"")
            if "Microscope" in message:
                sendMessage(s,"To move stage for 10 pixels, type command: \"move_x 10\", \"move_y 10\", \"move_y 10\", \"move_y 10\"")
            if "?" in message:
                # success 
                # testingcontroller.testing()
                sendMessage(s,"Hello! :) This is ScopyBot! How can I help you? -Below are several things that I can help you 1.Type \"Microscope\" or \"microscope\" to learn how to operate the microscpe 2. Type \"?\" to seek help 3. Type \"illumination\" to control lighting B)")
                break