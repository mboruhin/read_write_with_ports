import socket


def Main():
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)  #'192.168.0.13'  # client ip
    print(host)
    port = 4005

    # server = ('192.168.0.12', 4100)
    # server = (host, 4100)
    server = ('10.42.132.16', 4100)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.bind((host, port))

    message = input("-> ")
    while message != 'q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)
        message = input("-> ")

    s.sendto(message.encode('utf-8'), server)
    s.close()


if __name__ == '__main__':
    Main()