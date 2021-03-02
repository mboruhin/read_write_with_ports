import socket

def Main():
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)  # '192.168.0.12'  # Server ip
    port = 4100

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    data = None
    while data != 'Q':
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message from: " + str(addr))
        print("From connected user: " + data)
        data = data.upper()
        print("Sending: " + data)
        s.sendto(data.encode('utf-8'), addr)
    s.close()


if __name__ == '__main__':
    Main()