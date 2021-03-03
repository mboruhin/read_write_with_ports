from socket import *


def tcp_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 4100))
    s.listen(5)

    while True:
        client, addr = s.accept()
        foo(client)
        client.close()


def foo(client):
    while True:
        inbytes = client.recv(1024)
        if inbytes:
            outbytes = bytes(str(inbytes).upper())
            client.send(outbytes)


if __name__ == '__main__':
    tcp_server()