from socket import * 
import argparse

prs = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                description="""TCP Server""")                   
prs.add_argument("-port", dest="port", type=int, help="Server port.\n")
args = prs.parse_args()

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = args.port

# Bind the socket to server address and server port
serverSocket.bind(('127.0.0.1', serverPort))

serverSocket.listen(1)
while True:
    print('The server is ready to receive')

    conn, addr = serverSocket.accept()
    with conn:
        print('Connected by: ' + str(addr))
        while True:
            data = conn.recv(1024)
            if data:
                print(repr(data))

serverSocket.close()  