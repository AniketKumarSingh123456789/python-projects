import socket,threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()),9999))
s.listen(50)
conn,addr = s.accept()
def recv():
    while True:
        try:
            received_data =  conn.recv(1024)
            if received_data!='':
                print(received_data.decode('utf-8'))
        except:
            pass
receive = threading.Thread(target=recv)
receive.daemon = 1
receive.start()
while True:
    data = input()
    conn.send(bytes(data,encoding='utf-8'))