from mission_lobby import Ml
from delegate import Delegate
from pickup import Pickup

class Lobby_R:
    def __init__(self,socket):
        self.m=Ml(socket)
        self.d=Delegate(socket)
        self.p=Pickup(socket)

    def setlobby(self,number,window): # 創建layout
        if number==0: # 任務大廳
            self.m.setup(window)
        elif number==1: # 發佈過的任務
            self.d.setup(window)
        elif number==2: # 接取過的任務
            self.p.setup(window)
    
    def deletelobby(self,number): # 刪除layout
        if number==0:
            self.m.delete()
        elif number==1:
            self.d.delete()
        elif number==2:
            self.p.delete()