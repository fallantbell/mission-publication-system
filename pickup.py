# 接取過的任務
import tkinter as tk

class Pickup:
    def __init__(self,socket):
        self.socket=socket

        self.pickup_canvas=tk.Canvas()
        self.pickup_title_label=tk.Label()

    def setup(self,window):
        self.pickup_canvas=tk.Canvas(width=400,height=700,bg="blue")
        self.pickup_canvas.place(x=200,y=0)

        self.pickup_title_label=tk.Label(window,font="微軟正黑體 16 bold",relief="ridge",bd=2,width=31,height=4,fg="white",bg="cornflowerblue",text="接收的任務")
        self.pickup_title_label.place(x=200,y=0)
    
    def delete(self):
        self.pickup_canvas.place_forget()
        self.pickup_title_label.place_forget()