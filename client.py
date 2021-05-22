import socket
import tkinter as tk
import tkinter.font as tkFont
import threading
import time


HOST="127.0.0.1"
PORT=8080
DISCONNECT_MESSAGE="disconnect"
ADDR=(HOST,PORT)

# clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # <===================建立socket  
# clientsocket.connect(ADDR)

def registback(): # 返回登入畫面    
    deletregistlayout()
    setuserentrylayout()

def regist(): #註冊
    global registname,registpass
    if registname.get()=="":
        print("username cannt be empty!!")
        # registerror.set("username cannt be empty!!")
        # registerrorlabel.place(x=300,y=420)
    elif registpass.get()=="":
        print("password cannt be empty!!")
        # registerror.set("password cannt be empty!!")
        # registerrorlabel.place(x=300,y=420)
    else:
        msg="regist "+registname.get()+" "+registpass.get()
        # clientsocket.send(msg.encode())                  # <========================= 向server 傳遞註冊資料

def deletregistlayout(): #清除註冊介面
    global registcanvas,registnameentry,registpassentry,registbackbutton,registbutton
    registcanvas.place_forget()
    registnameentry.place_forget()
    registpassentry.place_forget()
    registbackbutton.place_forget()
    registbutton.place_forget()

def setregistlayout(): # 設置註冊介面
    global registcanvas,registnameimg,registpassimg,registnameentry,registpassentry,registbackbutton,registbutton

    registcanvas=tk.Canvas(width=600,height=700,bg="NavajoWhite")
    registcanvas.place(x=0,y=0)

    registnameimg=tk.PhotoImage(file="image/userimg.png")
    registcanvas.create_image(128,345,image=registnameimg)
    registpassimg=tk.PhotoImage(file="image/passimg.png")
    registcanvas.create_image(130,420,image=registpassimg)

    registnameentry=tk.Entry(window,bd=3,width=35,textvariable=registname)
    registnameentry.place(x=190,y=327,height=30)
    registpassentry=tk.Entry(window,bd=3,width=35,textvariable=registpass)
    registpassentry.place(x=190,y=407,height=30)

    registbackbutton=tk.Button(window,text="返回",command = registback)
    registbackbutton.place(x=180,y=470)
    registbutton=tk.Button(window,text="確認",command = regist)
    registbutton.place(x=260,y=470)


def enter(): # 登入
    global entername,enterpass
    
    if entername.get()=="":
        print("username cannt be empty!")
        # entererror.set("username cannt be empty!")
        # entererrorlabel.place(x=600,y=415)
    elif enterpass.get()=="":
        print("password cannt be empty!")
        # entererror.set("password cannt be empty!")
        # entererrorlabel.place(x=600,y=415)
    else:
        msg="enter "+entername.get()+" "+enterpass.get()
        # clientsocket.send(msg.encode())   #<================================ 向server 傳遞登入資料

def enterregist(): # 進入註冊畫面
    deleteuserentrylayout()
    setregistlayout()


def setuserentrylayout(): # 設置登入介面
    global entry_canvas,entry_title_img,usrnameentrybutton,usrregistbutton,usrpassentry,usrnameentry,usrnameimg,usrpassimg,enterimg,registimg
    entry_canvas=tk.Canvas(width=600,height=700,bg="NavajoWhite")
    entry_canvas.place(x=0,y=0)
    entry_title_img=tk.PhotoImage(file="image/titleimage.png")
    entry_canvas.create_image(300,150,image=entry_title_img)

    usrnameimg=tk.PhotoImage(file="image/userimg.png")
    entry_canvas.create_image(128,345,image=usrnameimg)
    usrpassimg=tk.PhotoImage(file="image/passimg.png")
    entry_canvas.create_image(130,420,image=usrpassimg)

    usrnameentry=tk.Entry(window,bd=3,width=35,textvariable=entername)
    usrnameentry.place(x=190,y=327,height=30)
    usrpassentry=tk.Entry(window,show='*',bd=3,width=35,textvariable=enterpass)
    usrpassentry.place(x=190,y=407,height=30)

    enterimg=tk.PhotoImage(file="image/enterimg.png")
    registimg=tk.PhotoImage(file="image/registimg.png")

    usrnameentrybutton=tk.Button(window,image=enterimg,relief="flat",bd=0,bg="NavajoWhite",highlightbackground="NavajoWhite",width=110,height=45,command = enter)
    usrnameentrybutton.place(x=180,y=455)
    usrregistbutton=tk.Button(window,image=registimg,relief="flat",bd=0,bg="NavajoWhite",highlightbackground="NavajoWhite",width=110,height=45,command = enterregist)
    usrregistbutton.place(x=310,y=453)

def deleteuserentrylayout(): # 清除登入介面
    global entry_canvas,usrnameentrybutton,usrregistbutton,usrpassentry,usrnameentry
    entry_canvas.place_forget()
    usrnameentrybutton.place_forget()
    usrregistbutton.place_forget()
    usrpassentry.place_forget()
    usrnameentry.place_forget()

window=tk.Tk()
window.geometry('600x700')
window.title("mission publication")

# 登入介面宣告
usrnameentry=tk.Entry()
usrpassentry=tk.Entry()
usrnameentrybutton=tk.Button()
usrregistbutton=tk.Button()
entry_canvas=tk.Canvas()
entry_title_img=tk.PhotoImage()
usrnameimg=tk.PhotoImage()
usrpassimg=tk.PhotoImage()
enterimg=tk.PhotoImage()
registimg=tk.PhotoImage()

entername=tk.StringVar()
enterpass=tk.StringVar()



#註冊介面宣告
registcanvas=tk.Canvas()
registnameimg=tk.PhotoImage()
registpassimg=tk.PhotoImage()
registnameentry=tk.Entry()
registpassentry=tk.Entry()
registbackbutton=tk.Button()
registbutton=tk.Button()

registname=tk.StringVar()
registpass=tk.StringVar()

#進入登入介面
setuserentrylayout()

def onclose():
    # clientsocket.send(DISCONNECT_MESSAGE.encode())
    # pygame.mixer.music.stop()
    window.destroy()

window.protocol("WM_DELETE_WINDOW",onclose)
window.mainloop()