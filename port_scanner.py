import pyfiglet
import sys
import argparse
from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket, gethostbyname
from datetime import datetime

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)



# Create argument parser for Port Scanner program
parser = argparse.ArgumentParser(
    prog = 'Port Scanner',
    description = 'Scans range of ports for an application or remote host',
    epilog = 'HEre'
)

parser.add_argument('-target', dest= 'host', type=str, help='Domain name of the target application, host', default='localhost')
parser.add_argument('-from-port', dest= 'first_port', type=int, help = 'First port of port range', default=1)
parser.add_argument('-to-port', dest='last_port', type=int, help='Last port of port range', required=True)


args = parser.parse_args()

# Range of ports that will be scanned
ports= range(args.first_port,args.last_port)


# check if can connect to specific port
def test_port_number(host, port): 
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(1)
        try:
            start = datetime.now()
            sock.connect((host,port))
            print(f'Connection time: {datetime.now()-start}')
            return True
        except:
            print(f'Connection time: {datetime.now()-start}')
            return False


def port_scan(host, ports):
    # Add Banner
    print("-" * 50)
    print("Scanning Target: " + host)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)
    for port in ports:
        try:
            if test_port_number(host, port):
                print(f'> {host}:{port} open')
        except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
        except socket.gaierror:
                print("\n Hostname Could Not Be Resolved !!!!")
                sys.exit()
        except socket.error:
                print("\ Server not responding !!!!")
                sys.exit()
    
port_scan(args.host, ports)


# try: 

#     # scan the port range 1-3000
#     for port in range(1, 5):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         socket.setdefaulttimeout(1)

#         # connect to target and return an error if not open
#         print("Scanning PORT ")
#         start = datetime.now()
#         result = s.connect_ex((target,port))
#         print(datetime.now()-start)
#         if result ==0:
#             print("Port {} is open".format(port))
#         s.close()
