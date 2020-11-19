import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():
	
    s = socket.socket()
    s.connect((HOST, PORT))
 
    output = "PASS "
    output2 = "\r\n"
    output3 = "Nick "
    output4 = "IDENT"
    output5 = "JOIN #"
    output6 = " CHANNEL"
    
    s.send(bytes("PASS " + PASS + "\r\n", 'UTF-8'))
    s.send(bytes("NICK " + IDENT + "\r\n", 'UTF-8'))
    s.send(bytes("JOIN #" + CHANNEL + "\r\n", 'UTF-8'))


    
#    s.sendall(output.encode('utf-8') + PASS + output2.encode('utf-8'))
#
#    s.sendall(output3.encode('utf-8') + IDENT + output2.encode('utf-8'))
#
#    s.sendall(output5.encode('utf-8') + CHANNEL + output2.encode('utf-8'))
#
#	s.send("PASS " + "PASS" + "\r\n")
#	s.send("NICK " + "IDENT" + "\r\n")
#	s.send("JOIN #" + " CHANNEL" + "\r\n")
    return s
	
def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    
    s.send(bytes(messageTemp + "\r\n", 'UTF-8'))

#	s.send(messageTemp + "\r\n")
    print("Sent: " + messageTemp)
