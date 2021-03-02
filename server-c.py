import socket

def Main():
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)  # '192.168.0.12'  # Server ip
    print(str(host))
    port = 4100

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    data = None
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message from: " + str(addr))
        print("From connected user: " + data)
        if data == 'q':
            break
        data = data.upper()
        print("Sending: " + data)
        s.sendto(data.encode('utf-8'), addr)
    s.close()


if __name__ == '__main__':
    Main()