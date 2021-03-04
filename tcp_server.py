from socket import *


def tcp_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 4100))
    s.listen(5)

    while True:
        client, addr = s.accept()
        print("server received message from:", client, addr)
        foo(client)
        client.close()


def foo(client):
    while True:
        inbytes = client.recv(1024)
        if inbytes:
            outbytes = inbytes.upper()
            print("sending:", outbytes)
            client.send(outbytes)
        else:
            print("breaking")
            break


if __name__ == '__main__':
    print('starting TCP server')
    tcp_server()
