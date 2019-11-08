from socket import * 
import time
import argparse


prs = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                description="""TCP Client""")

prs.add_argument("-destport", dest="destport", type=int, help="Server port.\n")
prs.add_argument("-destip", dest="destip", type=str, help="Server IP.\n")
args = prs.parse_args()

addr = (args.destip, args.destport)
packet = bytearray(1250)

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(addr)
    print('Connected to: ' + str(addr))

    while True:
        s.send(packet)
        

