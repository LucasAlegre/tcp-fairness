
import os
import errno
import argparse
import time
import csv
from threading import Thread
from socket import * 

DELTA = 0.1

def log_to_csv(log, client_addr):
	path = 'results/' + "client_" + client_addr[0].replace('.', '-') + "_" + str(client_addr[1]) + ".csv"
	with open(path, mode='w') as csv_log:
		log_writer = csv.writer(csv_log, delimiter=',')
		log_writer.writerow(["time", "bits/s"])
		for row in log:
			log_writer.writerow(row)

def listen_to_client(connection, addr):
    print('Connected by: ' + str(addr))

    bytes_read = 0
    log = []

    prev_time = time.time()
    elapsed_time = prev_time
    while True:
        try:
            data = connection.recv(65536)
            bytes_read += len(data)
            if not data:
                print('Client', addr, 'exited.')
                break
        except:
            print('Client', addr, 'exited.')
            break
            
        elapsed_time = time.time() - prev_time
        if elapsed_time >= DELTA:
            bits_per_sec = (bytes_read*8)/elapsed_time
            print(str(addr) + ' Bits/s: ' + str(bits_per_sec))
            bytes_read = 0
            prev_time = time.time()
            elapsed_time = prev_time
            log.append([elapsed_time, bits_per_sec])

    connection.close()

    log_to_csv(log, addr)

def run_server(port):
    #(AF_INET is used for IPv4 protocols)
    #(SOCK_STREAM is used for TCP)
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Bind the socket to server address and server port
    serverSocket.bind(('', port))

    serverSocket.listen(10)
    print('The server is ready to receive')

    threads = []
    while True:
        conn, addr = serverSocket.accept()
        t = Thread(target=listen_to_client, args=[conn, addr])
        threads.append(t)
        t.start()
    serverSocket.close()

if __name__ == '__main__':

    prs = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                    description="""TCP Server""")                   
    prs.add_argument("-port", dest="port", type=int, default=60000, help="Server port.\n")
    args = prs.parse_args()

    run_server(args.port)


    
