import tkinter as tk

class Lobby_L:
    def __init__(self,socket,master):
        self.socket=socket
        self.master=master

        self.lobbychoose=0 # 現在選到誰

        self.lobby_choose_canvas=tk.Canvas()
        self.lobby_choose_lobbybt=tk.Button()
        self.lobby_choose_delegatebt=tk.Button()
        self.lobby_choose_pickupbt=tk.Button()
        self.lobby_choose_exit=tk.Button()

        self.lobby_choose_lobbyimg=tk.PhotoImage()
        self.lobby_choose_delegateimg=tk.PhotoImage()
        self.lobby_choose_pickupimg=tk.PhotoImage()
        self.lobby_choose_exitimg=tk.PhotoImage()
    
    def setlobbychooselayout(self,window): # 設置大廳左邊選擇欄
        self.lobby_choose_canvas=tk.Canvas(width=200,height=700,bg="seagreen")
        self.lobby_choose_canvas.place(x=0,y=0)

        self.init_lobby_choose_color()
        # lobbychoose=1
        # createlobby()

        self.lobby_choose_lobbyimg=tk.PhotoImage(file="image/lobby_choose_lobbyimg_red.png")
        self.lobby_choose_lobbybt=tk.Button(window,image=self.lobby_choose_lobbyimg,bd=0,width=200,height=100,command=self.createlobby)
        self.lobby_choose_lobbybt.place(x=0,y=200)

        self.lobby_choose_delegateimg=tk.PhotoImage(file="image/lobby_choose_delegateimg.png")
        self.lobby_choose_delegatebt=tk.Button(window,image=self.lobby_choose_delegateimg,bd=0,width=200,height=100,command=self.createdelegate)
        self.lobby_choose_delegatebt.place(x=0,y=300)

        self.lobby_choose_pickupimg=tk.PhotoImage(file="image/lobby_choose_pickupimg.png")
        self.lobby_choose_pickupbt=tk.Button(window,image=self.lobby_choose_pickupimg,bd=0,width=200,height=100,command=self.createpickup)
        self.lobby_choose_pickupbt.place(x=0,y=400)

        self.lobby_choose_exitimg=tk.PhotoImage(file="image/lobby_choose_exitimg.png")
        self.lobby_choose_exit=tk.Button(window,image=self.lobby_choose_exitimg,bd=0,width=200,height=100,command=self.lobbyexit)
        self.lobby_choose_exit.place(x=0,y=600)
    
    def init_lobby_choose_color(self): # 大廳左邊選擇欄初始白色
        self.lobby_choose_lobbyimg=tk.PhotoImage(file="image/lobby_choose_lobbyimg.png")
        self.lobby_choose_lobbybt["image"]=self.lobby_choose_lobbyimg

        self.lobby_choose_delegateimg=tk.PhotoImage(file="image/lobby_choose_delegateimg.png")
        self.lobby_choose_delegatebt["image"]=self.lobby_choose_delegateimg

        self.lobby_choose_pickupimg=tk.PhotoImage(file="image/lobby_choose_pickupimg.png")
        self.lobby_choose_pickupbt["image"]=self.lobby_choose_pickupimg

    def createlobby(self): # 設置接收的任務介面
        if self.lobbychoose==0: # 原本就在此介面
            return

        self.init_lobby_choose_color()
        self.lobbychoose=0

        # 改變選擇欄顏色
        self.lobby_choose_lobbyimg=tk.PhotoImage(file="image/lobby_choose_lobbyimg_red.png")
        self.lobby_choose_lobbybt["image"]=self.lobby_choose_lobbyimg

        # 設置接收的任務介面
        self.master.setlr(0)

    def createdelegate(self): # 設置發布的任務介面
        if self.lobbychoose==1: # 原本就在此介面
            return
    
        self.init_lobby_choose_color()
        self.lobbychoose=1   

        # 改變選擇欄顏色
        self.lobby_choose_delegateimg=tk.PhotoImage(file="image/lobby_choose_delegateimg_red.png")
        self.lobby_choose_delegatebt["image"]=self.lobby_choose_delegateimg

        # 設置發布的任務介面
        self.master.setlr(1)
        
    def createpickup(self): # 設置接收的任務介面
        if self.lobbychoose==2: # 原本就在此介面
            return

        self.lobbychoose=2
        self.init_lobby_choose_color()

        # 改變選擇欄顏色
        self.lobby_choose_pickupimg=tk.PhotoImage(file="image/lobby_choose_pickupimg_red.png")
        self.lobby_choose_pickupbt["image"]=self.lobby_choose_pickupimg

        # 設置接收的任務介面
        self.master.setlr(2)

    def lobbyexit(self):
        pass
