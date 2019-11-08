from socket import * 
import argparse
import time
import matplotlib.pyplot as plt


prs = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                description="""TCP Server""")                   
prs.add_argument("-port", dest="port", type=int, required=True, help="Server port.\n")
args = prs.parse_args()

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = args.port

# Bind the socket to server address and server port
serverSocket.bind(('127.0.0.1', serverPort))

serverSocket.listen(1)
print('The server is ready to receive')
total_bytes = 0
timer = 0
statistics = []
conn, addr = serverSocket.accept()
with conn:
    print('Connected by: ' + str(addr))

    while True:
        data = conn.recv(2000)
        total_bytes += len(data)
				
        timer += time.time()
				
        if timer % 1000 == 0:
            print('Read ' + str(total_bytes) + ' bytes.')
            statistics.append(total_bytes)
            total_bytes = 0
            if timer > 20000:
                plt.figure()
                plt.plot(statistics)
                plt.show()

serverSocket.close()  
