# 任務大廳
import tkinter as tk

class Ml:
    def __init__(self,socket):
        self.socket=socket

        self.lobby_canvs=tk.Canvas()
        self.lobby_delegatebt=tk.Button()
        self.lobby_title_label=tk.Label()


    def setup(self,window):
        self.lobby_canvs=tk.Canvas(width=400,height=700,bg="gainsboro")
        self.lobby_canvs.place(x=200,y=0)

        self.lobby_delegatebt=tk.Button(window,font="微軟正黑體 16 bold",relief="ridge",bd=2,width=30,height=2,activebackground="chocolate",activeforeground="white",fg="white",bg="sandybrown",text="發布任務")# ,command=delegating
        self.lobby_delegatebt.place(x=200,y=627)

        self.lobby_title_label=tk.Label(window,font="微軟正黑體 16 bold",relief="ridge",bd=2,width=31,height=4,fg="white",bg="cornflowerblue",text="任務大廳")
        self.lobby_title_label.place(x=200,y=0)
    
    def delete(self):
        self.lobby_canvs.place_forget()
        self.lobby_title_label.place_forget()
        self.lobby_delegatebt.place_forget()