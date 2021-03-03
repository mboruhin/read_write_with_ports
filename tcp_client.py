import sys
from socket import *

server_ip = '10.42.132.16'

if len(sys.argv) < 2:
    sys.stderr.write("usage: %s host service args...\n" % sys.args[0])
    raise SystemExit(1)

s = socket(AF_INET, SOCK_STREAM)
port = 4100
s.connect((server_ip, port))

for message in sys.argv[1:]:
    s.send(message.encode('ascii'))
    response = s.recv(len(message))
    print(response.decode(), end=' ')

s.close()
print()
