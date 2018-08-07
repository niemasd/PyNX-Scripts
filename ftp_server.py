# fix errno
import errno
errno.ESHUTDOWN = 58

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from sys import stdout
import socket

USER='switch'
PASS='switch'
PORT=21
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
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous(ROOTDIR)
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(('', PORT), handler)
    stdout.write("FTP Server is running on %s:%d\n" % (get_ip(),PORT)); stdout.flush()
    server.serve_forever()
