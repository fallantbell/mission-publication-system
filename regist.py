import tkinter as tk

class Regist:
    def __init__(self,socket):
        self.registcanvas=tk.Canvas()
        self.registnameimg=tk.PhotoImage()
        self.registpassimg=tk.PhotoImage()
        self.registnameentry=tk.Entry()
        self.registpassentry=tk.Entry()
        self.registbackbutton=tk.Button()
        self.registbutton=tk.Button()

        self.registname=tk.StringVar()
        self.registpass=tk.StringVar()

        self.socket=socket

    def setregistlayout(self,window,master): # 設置註冊介面
        # global registcanvas,registnameimg,registpassimg,registnameentry,registpassentry,registbackbutton,registbutton

        self.registcanvas=tk.Canvas(width=600,height=700,bg="NavajoWhite")
        self.registcanvas.place(x=0,y=0)

        self.registnameimg=tk.PhotoImage(file="image/userimg.png")
        self.registcanvas.create_image(128,345,image=self.registnameimg)
        self.registpassimg=tk.PhotoImage(file="image/passimg.png")
        self.registcanvas.create_image(130,420,image=self.registpassimg)

        self.registnameentry=tk.Entry(window,font="微軟正黑體 16 bold",bd=3,width=20,textvariable=self.registname)
        self.registnameentry.place(x=190,y=327,height=30)
        self.registpassentry=tk.Entry(window,font="微軟正黑體 16 bold",bd=3,width=20,textvariable=self.registpass)
        self.registpassentry.place(x=190,y=407,height=30)

        self.registbackbutton=tk.Button(window,text="返回",command=lambda: master.registtoentry())
        self.registbackbutton.place(x=180,y=470)
        self.registbutton=tk.Button(window,text="確認",command=self.send)
        self.registbutton.place(x=260,y=470)

    def deleteregistlayout(self): #清除註冊介面
        # global registcanvas,registnameentry,registpassentry,registbackbutton,registbutton
        self.registcanvas.place_forget()
        self.registnameentry.place_forget()
        self.registpassentry.place_forget()
        self.registbackbutton.place_forget()
        self.registbutton.place_forget()
    
    def send(self):
        if self.registname.get()=="":
            print("username cannt be empty!!")
        elif self.registpass.get()=="":
            print("password cannt be empty!!")
        else:
            msg="regist signin "+self.registname.get()+" "+self.registpass.get()
            self.registname.set("")
            self.registpass.set("")
            self.socket.send(msg.encode())  