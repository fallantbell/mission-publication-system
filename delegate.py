# 發布過的任務
import tkinter as tk

class Delegate:
    def __init__(self,socket):
        self.socket=socket

        self.delegate_canvas=tk.Canvas()
        self.delegate_title_label=tk.Label()
    
    def setup(self,window):
        self.delegate_canvas=tk.Canvas(width=400,height=700,bg="red")
        self.delegate_canvas.place(x=200,y=0)

        self.delegate_title_label=tk.Label(window,font="微軟正黑體 16 bold",relief="ridge",bd=2,width=31,height=4,fg="white",bg="cornflowerblue",text="發布的任務")
        self.delegate_title_label.place(x=200,y=0)
    
    def delete(self):
        self.delegate_canvas.place_forget()
        self.delegate_title_label.place_forget()