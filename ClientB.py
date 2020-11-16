import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = raw_input("tcpClientB: Enter message/ Enter exit:") 
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

while MESSAGE != 'exit':
    tcpClientB.send(MESSAGE)     
    data = tcpClientB.recv(BUFFER_SIZE)
    equ=input("Please give me your equation (Ex: 2+2) or Q to quit: ")
    s.send(equ.encode())
    result = s.recv(1024).decode()
    if result == "Quit":
            print("Closing client connection, goodbye")
            break
    elif result == "ZeroDiv":
            print("You can't divide by 0, try again")
    elif result == "MathError":
            print("There is an error with your math, try again")
    elif result == "SyntaxError":
            print("There is a syntax error, please try again")
    elif result == "NameError":
            print("You did not enter an equation, try again")
    else:
            print("The answer is:", result)
    print " Client2 received data:", data
    MESSAGE = raw_input("tcpClientA: Enter message to continue/ Enter exit:")

tcpClientB.close() 
