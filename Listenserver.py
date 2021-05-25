import threading
from switchlayout import Switch

class Lserver(threading.Thread):
    def __init__(self,clientsocket,switch):
        threading.Thread.__init__(self)
        self.socket=clientsocket
        self.switch=switch


    def run(self):
        while True:
            x=self.socket.recv(1024).decode() 
            x=x.split(" ")
            if x[0]=="go":
                self.switch.entrytolobby()

