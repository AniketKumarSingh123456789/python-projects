import socket,threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.56.1',9999))
def recv2():
    while True:
        try:
            received_data = s.recv(1024)
            if received_data!='':
                print(received_data.decode('utf-8'))
        except:
            pass
receive = threading.Thread(target=recv2)
receive.daemon = 1
receive.start()
while True:
    data = input()
    s.send(bytes(data,encoding='utf-8'))