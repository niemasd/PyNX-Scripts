from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import chdir
from sys import stdout
import socket
PORT=8000
ROOTDIR='/'

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == '__main__':
    chdir(ROOTDIR)
    server_address = ('',PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    stdout.write("HTTP Server is running on %s:%d\n" % (get_ip(),PORT)); stdout.flush()
    httpd.serve_forever()
