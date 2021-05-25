import socket
import tkinter as tk
from Listenserver import Lserver
from switchlayout import Switch


if __name__ == '__main__':
    window=tk.Tk()
    window.geometry('600x700')
    window.title("mission publication")

    HOST="127.0.0.1"
    PORT=8080
    DISCONNECT_MESSAGE="disconnect"
    ADDR=(HOST,PORT)

    clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 建立socket  
    clientsocket.connect(ADDR)

    s=Switch(window,clientsocket) # 主線程
    L=Lserver(clientsocket,s).start() #thread 監聽server

    window.mainloop()