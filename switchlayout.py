# 轉換layout

from entry import Entry
from regist import Regist
from lobby import Lobby

class Switch:
    def __init__(self,window,socket):
        self.window=window
        self.e=Entry(socket)
        self.r=Regist(socket)
        self.l=Lobby(self.window,socket)
        self.e.setuserentrylayout(self.window,self)

    def entrytoregist(self):
        self.e.deleteuserentrylayout()
        self.r.setregistlayout(self.window,self)

    def registtoentry(self):
        self.r.deleteregistlayout()
        self.e.setuserentrylayout(self.window,self)

    def entrytolobby(self):
        self.e.deleteuserentrylayout()
        self.l.setlobbylayout()

