from lobby_l import Lobby_L
from lobby_r import Lobby_R

class Lobby:
    def __init__(self,window,socket):
        self.window=window
        self.socket=socket
        self.l=Lobby_L(socket,self)
        self.r=Lobby_R(socket)

        self.rnum=0 # 第幾個功能
        
    
    def setlobbylayout(self): # 建立大廳
        self.l.setlobbychooselayout(self.window)
        self.r.setlobby(self.rnum,self.window)

    def setlr(self,number): #number 為換到新的功能編號  (lobby_l 內保證number != rnum)
        self.r.deletelobby(self.rnum) # 刪除舊介面
        self.r.setlobby(number,self.window) #新增新介面
        self.rnum=number # 更新編號
        