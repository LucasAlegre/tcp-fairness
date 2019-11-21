from socket import socket, AF_INET, SOCK_STREAM
import time
import argparse


def run_client(address):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(addr)
    print('Connected to: ' + str(addr))

    packet = bytearray(1250)
    while True:
        client_socket.send(packet)

    client_socket.close()
    

if __name__ == '__main__':

    prs = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                    description="""TCP Client""")

    prs.add_argument("-port", dest="destport", type=int, required=True, help="Server port.\n")
    prs.add_argument("-ip", dest="destip", type=str, default='localhost', help="Server IP.\n")
    args = prs.parse_args()

    addr = (args.destip, args.destport)
    
    run_client(addr)
