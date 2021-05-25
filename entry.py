import tkinter as tk

class Entry:
    def __init__(self,socket):
        self.usrnameentry=tk.Entry()
        self.usrpassentry=tk.Entry()
        self.usrnameentrybutton=tk.Button()
        self.usrregistbutton=tk.Button()
        self.entry_canvas=tk.Canvas()
        self.entry_title_img=tk.PhotoImage()
        self.usrnameimg=tk.PhotoImage()
        self.usrpassimg=tk.PhotoImage()
        self.enterimg=tk.PhotoImage()
        self.registimg=tk.PhotoImage()

        self.entername=tk.StringVar()
        self.enterpass=tk.StringVar()

        self.socket=socket
    def setuserentrylayout(self,window,master): # 設置登入介面
        # global entry_canvas,entry_title_img,usrnameentrybutton,usrregistbutton,usrpassentry,usrnameentry,usrnameimg,usrpassimg,enterimg,registimg
        self.entry_canvas=tk.Canvas(width=600,height=700,bg="NavajoWhite")
        self.entry_canvas.place(x=0,y=0)
        self.entry_title_img=tk.PhotoImage(file="image/titleimage.png")
        self.entry_canvas.create_image(300,150,image=self.entry_title_img)

        self.usrnameimg=tk.PhotoImage(file="image/userimg.png")
        self.entry_canvas.create_image(128,345,image=self.usrnameimg)
        self.usrpassimg=tk.PhotoImage(file="image/passimg.png")
        self.entry_canvas.create_image(130,420,image=self.usrpassimg)

        self.usrnameentry=tk.Entry(window,font="微軟正黑體 16 bold",bd=3,width=20,textvariable=self.entername)
        self.usrnameentry.place(x=190,y=327,height=30)
        self.usrpassentry=tk.Entry(window,font="微軟正黑體 16 bold",show='*',bd=3,width=20,textvariable=self.enterpass)
        self.usrpassentry.place(x=190,y=407,height=30)

        self.enterimg=tk.PhotoImage(file="image/enterimg.png")
        self.registimg=tk.PhotoImage(file="image/registimg.png")

        self.usrnameentrybutton=tk.Button(window,image=self.enterimg,relief="flat",bd=0,bg="NavajoWhite",highlightbackground="NavajoWhite",width=110,height=45,command=self.send)
        self.usrnameentrybutton.place(x=180,y=455)
        self.usrregistbutton=tk.Button(window,image=self.registimg,relief="flat",bd=0,bg="NavajoWhite",highlightbackground="NavajoWhite",width=110,height=45,command=lambda:master.entrytoregist())
        self.usrregistbutton.place(x=310,y=453)

    def deleteuserentrylayout(self): # 清除登入介面
        # global entry_canvas,usrnameentrybutton,usrregistbutton,usrpassentry,usrnameentry
        self.entry_canvas.place_forget()
        self.usrnameentrybutton.place_forget()
        self.usrregistbutton.place_forget()
        self.usrpassentry.place_forget()
        self.usrnameentry.place_forget()

    def send(self):
        if self.entername.get()=="":
            print("username cannt be empty!")
        elif self.enterpass.get()=="":
            print("password cannt be empty!")
        else:
            msg="account signin "+self.entername.get()+" "+self.enterpass.get()
            self.entername.set("")
            self.enterpass.set("")
            self.socket.send(msg.encode())