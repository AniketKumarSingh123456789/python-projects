import socket,threading,json,mysql.connector
from tkinter import ttk,messagebox,filedialog
from tkinter import *

#######################  Main window  ###########################
chat_app = Tk()

chat_app.mainloop()
# ###########################  MYSQL CONECTION #############################
# conn = mysql.connector.connect(host='localhost', user='root',passwd='aniket')
# cur = conn.cursor()
# conn.commit()
# conn.close()
# with open('config.json') as f:
#     info = json.load(f)["info"]

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect((info["ip_addr"],9999))
# def recv2():
#     while True:
#         try:
#             received_data = s.recv(1024)
#             if received_data!='':
#                 print("Your friend => ",received_data.decode('utf-8'))
#         except:
#             pass
# receive = threading.Thread(target=recv2)
# receive.daemon = 1
# receive.start()
# while True:
#     data = input("You => ")
#     s.send(bytes(data,encoding='utf-8'))