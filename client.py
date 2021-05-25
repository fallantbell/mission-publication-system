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

lobbychoose=1 # 0=lobby 1=delegate 2=pickup  
username="username"

def sendmission(): #使用者發布任務
    ## 送資料到server
    delegatetolobby()

def delegatetolobby(): # 發布任務介面返回大聽
    delete_user_delegate_layout()
    setlobbychooselayout()

def delete_user_delegate_layout(): # 刪除發布任務介面
    global user_delegate_content_lb,user_delegate_missionname_lb,user_delegate_money_lb,user_delegate_place_lb,user_delegate_time_lb,user_delegate_user_lb   
    global user_delegate_content_text,user_delegate_missionname_entry,user_delegate_money_entry,user_delegate_place_entry,user_delegate_time_entry
    global user_delegate_content,user_delegate_missionname,user_delegate_money,user_delegate_place,user_delegate_time
    global user_delegate_canvas,username,user_delegate_backimg,userdelegate_backbt,userdelegate_sendbt

    user_delegate_content.set("")
    user_delegate_missionname.set("")
    user_delegate_money.set("")
    user_delegate_place.set("")
    user_delegate_time.set("")

    user_delegate_user_lb.place_forget()
    user_delegate_content_lb.place_forget()
    user_delegate_missionname_lb.place_forget()
    user_delegate_money_lb.place_forget()
    user_delegate_place_lb.place_forget()
    user_delegate_time_lb.place_forget()

    user_delegate_content_text.place_forget()
    user_delegate_missionname_entry.place_forget()
    user_delegate_money_entry.place_forget()
    user_delegate_place_entry.place_forget()
    user_delegate_time_entry.place_forget()

    userdelegate_backbt.place_forget()
    user_delegate_canvas.place_forget()
    userdelegate_sendbt.place_forget()


def set_user_delegate_layout(): # 建立發布任務介面
    global user_delegate_content_lb,user_delegate_missionname_lb,user_delegate_money_lb,user_delegate_place_lb,user_delegate_time_lb,user_delegate_user_lb   
    global user_delegate_content_text,user_delegate_missionname_entry,user_delegate_money_entry,user_delegate_place_entry,user_delegate_time_entry
    global user_delegate_content,user_delegate_missionname,user_delegate_money,user_delegate_place,user_delegate_time
    global user_delegate_canvas,username,user_delegate_backimg,userdelegate_backbt,userdelegate_sendbt,user_delegate_sendimg
    user_delegate_canvas=tk.Canvas(width=600,height=700,bg="NavajoWhite")
    user_delegate_canvas.place(x=0,y=0)

    user_delegate_user_lb=tk.Label(window,font="微軟正黑體 16 bold",bg="NavajoWhite",text="發佈人:"+username)
    user_delegate_user_lb.place(x=20,y=70)
    user_delegate_missionname_lb=tk.Label(window,font="微軟正黑體 16 bold",bg="NavajoWhite",text="任務名稱:")
    user_delegate_missionname_lb.place(x=20,y=120)
    user_delegate_place_lb=tk.Label(window,font="微軟正黑體 16 bold",bg="NavajoWhite",text="任務地點:")
    user_delegate_place_lb.place(x=20,y=170)
    user_delegate_time_lb=tk.Label(window,font="微軟正黑體 16 bold",bg="NavajoWhite",text="時間:")
    user_delegate_time_lb.place(x=20,y=220)
    user_delegate_money_lb=tk.Label(window,font="微軟正黑體 16 bold",bg="NavajoWhite",text="酬勞:")
    user_delegate_money_lb.place(x=20,y=270)
    user_delegate_content_lb=tk.Label(window,font="微軟正黑體 16 bold",bg="NavajoWhite",text="任務內容:")
    user_delegate_content_lb.place(x=20,y=320)

    user_delegate_missionname_entry=tk.Entry(window,font="微軟正黑體 16 bold",bd=1,width=25,textvariable=user_delegate_missionname)
    user_delegate_missionname_entry.place(x=130,y=125)
    user_delegate_place_entry=tk.Entry(window,font="微軟正黑體 16 bold",bd=1,width=25,textvariable=user_delegate_place)
    user_delegate_place_entry.place(x=130,y=175)
    user_delegate_time_entry=tk.Entry(window,font="微軟正黑體 16 bold",bd=1,width=25,textvariable=user_delegate_time)
    user_delegate_time_entry.place(x=130,y=225)
    user_delegate_money_entry=tk.Entry(window,font="微軟正黑體 16 bold",bd=1,width=25,textvariable=user_delegate_money)
    user_delegate_money_entry.place(x=130,y=275)
    user_delegate_content_text=tk.Text(window,font="微軟正黑體 16 bold",bd=1,width=40,height=10)
    user_delegate_content_text.place(x=20,y=370)

    user_delegate_backimg=tk.PhotoImage(file="image/back.png")
    userdelegate_backbt=tk.Button(window,image=user_delegate_backimg,relief="flat",bd=0,width=100,height=50,command=delegatetolobby)
    userdelegate_backbt.place(x=18,y=15)

    user_delegate_sendimg=tk.PhotoImage(file="image/user_delegate_sendimg.png")
    userdelegate_sendbt=tk.Button(window,image=user_delegate_sendimg,relief="flat",bd=0,width=240,height=50,command=sendmission)
    userdelegate_sendbt.place(x=175,y=650)

def delegating(): # 使用者發布任務
    delete_lobby_right()
    deletelobbychooselayout()
    set_user_delegate_layout()


def init_lobby_choose_color(): # 大廳左邊選擇欄初始白色
    global lobby_choose_lobbyimg,lobby_choose_lobbybt,lobby_choose_delegateimg,lobby_choose_delegatebt,lobby_choose_pickupimg,lobby_choose_pickupbt
    lobby_choose_lobbyimg=tk.PhotoImage(file="image/lobby_choose_lobbyimg.png")
    lobby_choose_lobbybt["image"]=lobby_choose_lobbyimg

    lobby_choose_delegateimg=tk.PhotoImage(file="image/lobby_choose_delegateimg.png")
    lobby_choose_delegatebt["image"]=lobby_choose_delegateimg

    lobby_choose_pickupimg=tk.PhotoImage(file="image/lobby_choose_pickupimg.png")
    lobby_choose_pickupbt["image"]=lobby_choose_pickupimg

def delete_lobby_right(): #刪除大廳右側的layout
    global lobbychoose
    if lobbychoose==0:
        deletelobby()
    elif lobbychoose==1:
        deletedelegate()
    elif lobbychoose==2:
        deletepickup()

def lobbyexit(): # 離開 回到登入介面
    deletelobbychooselayout()
    setuserentrylayout()

def deletepickup(): # 刪除接收的任務介面
    global pickup_canvas,pickup_title_label
    pickup_canvas.place_forget()
    pickup_title_label.place_forget()

def createpickup(): # 設置接收的任務介面
    global lobbychoose,lobby_choose_pickupimg,lobby_choose_pickupbt
    global pickup_canvas,pickup_title_label
    if lobbychoose==2:
        return

    delete_lobby_right()
    lobbychoose=2
    init_lobby_choose_color()

    # 改變選擇欄顏色
    lobby_choose_pickupimg=tk.PhotoImage(file="image/lobby_choose_pickupimg_red.png")
    lobby_choose_pickupbt["image"]=lobby_choose_pickupimg

    # 設置接收的任務介面
    pickup_canvas=tk.Canvas(width=400,height=700,bg="blue")
    pickup_canvas.place(x=200,y=0)

    pickup_title_label=tk.Label(window,font="微軟正黑體 16 bold",relief="ridge",bd=2,width=31,height=4,fg="white",bg="cornflowerblue",text="接收的任務")
    pickup_title_label.place(x=200,y=0)
    

def deletedelegate(): #刪除發布的任務介面
    global delegate_canvas,delegate_title_label
    delegate_canvas.place_forget()
    delegate_title_label.place_forget()

def createdelegate(): # 設置發布的任務介面
    global lobbychoose,lobby_choose_delegateimg,lobby_choose_delegatebt
    global delegate_canvas,delegate_title_label
    if lobbychoose==1:
        return
   
    delete_lobby_right() 
    init_lobby_choose_color()
    lobbychoose=1   

    # 改變選擇欄顏色
    init_lobby_choose_color()
    lobby_choose_delegateimg=tk.PhotoImage(file="image/lobby_choose_delegateimg_red.png")
    lobby_choose_delegatebt["image"]=lobby_choose_delegateimg

    # 設置發布的任務介面
    delegate_canvas=tk.Canvas(width=400,height=700,bg="red")
    delegate_canvas.place(x=200,y=0)

    delegate_title_label=tk.Label(window,font="微軟正黑體 16 bold",relief="ridge",bd=2,width=31,height=4,fg="white",bg="cornflowerblue",text="發布的任務")
    delegate_title_label.place(x=200,y=0)

def deletelobby(): # 刪除任務大廳介面
    global lobby_canvs,lobby_delegatebt,lobby_title_label
    lobby_canvs.place_forget()
    lobby_title_label.place_forget()
    lobby_delegatebt.place_forget()

def createlobby(): # 設置任務大廳介面
    global lobby_choose_lobbyimg,lobbychoose,lobby_choose_lobbybt
    global lobby_canvs,lobby_delegatebt,lobby_title_label
    if lobbychoose==0:
        return

    delete_lobby_right()
    init_lobby_choose_color()
    lobbychoose=0

    # 改變選擇欄顏色
    lobby_choose_lobbyimg=tk.PhotoImage(file="image/lobby_choose_lobbyimg_red.png")
    lobby_choose_lobbybt["image"]=lobby_choose_lobbyimg

    # 設置大廳
    lobby_canvs=tk.Canvas(width=400,height=700,bg="gainsboro")
    lobby_canvs.place(x=200,y=0)

    lobby_delegatebt=tk.Button(window,font="微軟正黑體 16 bold",relief="ridge",bd=2,width=30,height=2,activebackground="chocolate",activeforeground="white",fg="white",bg="sandybrown",text="發布任務",command=delegating)
    lobby_delegatebt.place(x=200,y=627)

    lobby_title_label=tk.Label(window,font="微軟正黑體 16 bold",relief="ridge",bd=2,width=31,height=4,fg="white",bg="cornflowerblue",text="任務大廳")
    lobby_title_label.place(x=200,y=0)


def deletelobbychooselayout(): # 清除大廳左邊選擇欄
    global lobby_choose_canvas,lobby_choose_delegatebt,lobby_choose_exit,lobby_choose_lobbybt,lobby_choose_pickupbt
    lobby_choose_canvas.place_forget()
    lobby_choose_delegatebt.place_forget()
    lobby_choose_exit.place_forget()
    lobby_choose_lobbybt.place_forget()
    lobby_choose_pickupbt.place_forget()

def setlobbychooselayout():  # 設置大廳左邊選擇欄
    global lobby_choose_canvas,lobby_choose_delegatebt,lobby_choose_exit,lobby_choose_lobbybt,lobby_choose_pickupbt,lobby_choose_pickupimg,lobby_choose_lobbyimg,lobby_choose_exitimg,lobby_choose_delegateimg
    global lobbychoose
    lobby_choose_canvas=tk.Canvas(width=200,height=700,bg="seagreen")
    lobby_choose_canvas.place(x=0,y=0)

    init_lobby_choose_color()
    lobbychoose=1
    createlobby()

    lobby_choose_lobbyimg=tk.PhotoImage(file="image/lobby_choose_lobbyimg_red.png")
    lobby_choose_lobbybt=tk.Button(window,image=lobby_choose_lobbyimg,bd=0,width=200,height=100,command=createlobby)
    lobby_choose_lobbybt.place(x=0,y=200)

    lobby_choose_delegateimg=tk.PhotoImage(file="image/lobby_choose_delegateimg.png")
    lobby_choose_delegatebt=tk.Button(window,image=lobby_choose_delegateimg,bd=0,width=200,height=100,command=createdelegate)
    lobby_choose_delegatebt.place(x=0,y=300)

    lobby_choose_pickupimg=tk.PhotoImage(file="image/lobby_choose_pickupimg.png")
    lobby_choose_pickupbt=tk.Button(window,image=lobby_choose_pickupimg,bd=0,width=200,height=100,command=createpickup)
    lobby_choose_pickupbt.place(x=0,y=400)

    lobby_choose_exitimg=tk.PhotoImage(file="image/lobby_choose_exitimg.png")
    lobby_choose_exit=tk.Button(window,image=lobby_choose_exitimg,bd=0,width=200,height=100,command=lobbyexit)
    lobby_choose_exit.place(x=0,y=600)

# def confirmname(): #確認暱稱
#     global setname,username
#     if setname.get()=="":
#         print("username cannt be empty!")
#     msg="setname "+setname.get()
#     username=setname.get()
#     setname.set("")
#     setlobbychooselayout()
#     deletesetnamelayout()
#     # clientsocket.send(msg.encode())                # <=====================傳遞暱稱到server

# def deletesetnamelayout(): #刪除設定暱稱layout
#     global setnamebt,setnamecanvas,setnameentry,setnameimg,setnametitleimg,setname
#     setnamebt.place_forget()
#     setnamecanvas.place_forget()
#     setnameentry.place_forget()


# def setsetnamelayout(): #建立設定暱稱layout
#     global setnamebt,setnamecanvas,setnameentry,setnameimg,setnametitleimg,setname
#     setnamecanvas=tk.Canvas(width=600,height=700,bg="NavajoWhite")
#     setnamecanvas.place(x=0,y=0)

#     setnameimg=tk.PhotoImage(file="image/setnameimg.png")
#     setnamecanvas.create_image(128,345,image=setnameimg)
#     setnametitleimg=tk.PhotoImage(file="image/setnametitleimg.png")
#     setnamecanvas.create_image(300,150,image=setnametitleimg)

#     setnameentry=tk.Entry(window,font="微軟正黑體 16 bold",bd=3,width=20,textvariable=setname)
#     setnameentry.place(x=190,y=327,height=30)

#     setnamebt=tk.Button(window,text="確認",command=confirmname)
#     setnamebt.place(x=180,y=470)



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
        registname.set("")
        registpass.set("")
        # clientsocket.send(msg.encode())                  # <========================= 向server 傳遞註冊資料

def deletregistlayout(): #清除註冊介面
    global registcanvas,registnameentry,registpassentry,registbackbutton,registbutton
    registcanvas.place_forget()
    registnameentry.place_forget()
    registpassentry.place_forget()
    registbackbutton.place_forget()
    registbutton.place_forget()

# def setregistlayout(): # 設置註冊介面
#     global registcanvas,registnameimg,registpassimg,registnameentry,registpassentry,registbackbutton,registbutton

#     registcanvas=tk.Canvas(width=600,height=700,bg="NavajoWhite")
#     registcanvas.place(x=0,y=0)

#     registnameimg=tk.PhotoImage(file="image/userimg.png")
#     registcanvas.create_image(128,345,image=registnameimg)
#     registpassimg=tk.PhotoImage(file="image/passimg.png")
#     registcanvas.create_image(130,420,image=registpassimg)

#     registnameentry=tk.Entry(window,font="微軟正黑體 16 bold",bd=3,width=20,textvariable=registname)
#     registnameentry.place(x=190,y=327,height=30)
#     registpassentry=tk.Entry(window,font="微軟正黑體 16 bold",bd=3,width=20,textvariable=registpass)
#     registpassentry.place(x=190,y=407,height=30)

#     registbackbutton=tk.Button(window,text="返回",command = registback)
#     registbackbutton.place(x=180,y=470)
#     registbutton=tk.Button(window,text="確認",command = regist)
#     registbutton.place(x=260,y=470)


def enter(): # 登入
    global entername,enterpass
    # setsetnamelayout()
    setlobbychooselayout()
    deleteuserentrylayout()
    if entername.get()=="":
        print("username cannt be empty!")
    elif enterpass.get()=="":
        print("password cannt be empty!")
    else:
        msg="account "+entername.get()+" "+enterpass.get()
        entername.set("")
        enterpass.set("")
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

    usrnameentry=tk.Entry(window,font="微軟正黑體 16 bold",bd=3,width=20,textvariable=entername)
    usrnameentry.place(x=190,y=327,height=30)
    usrpassentry=tk.Entry(window,font="微軟正黑體 16 bold",show='*',bd=3,width=20,textvariable=enterpass)
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


#設定暱稱宣告
setnamecanvas=tk.Canvas()
setnametitleimg=tk.PhotoImage()
setnameimg=tk.PhotoImage()
setnameentry=tk.Entry()
setnamebt=tk.Button()

setname=tk.StringVar()

#大廳選單宣告
lobby_choose_canvas=tk.Canvas()
lobby_choose_lobbybt=tk.Button()
lobby_choose_delegatebt=tk.Button()
lobby_choose_pickupbt=tk.Button()
lobby_choose_exit=tk.Button()

lobby_choose_lobbyimg=tk.PhotoImage()
lobby_choose_delegateimg=tk.PhotoImage()
lobby_choose_pickupimg=tk.PhotoImage()
lobby_choose_exitimg=tk.PhotoImage()

#大廳宣告
lobby_canvs=tk.Canvas()
lobby_delegatebt=tk.Button()
lobby_title_label=tk.Label()

#發布的任務宣告
delegate_canvas=tk.Canvas()
delegate_title_label=tk.Label()


#接收的任務宣告
pickup_canvas=tk.Canvas()
pickup_title_label=tk.Label()

#發布任務需告
user_delegate_canvas=tk.Canvas()
user_delegate_user_lb=tk.Label()
user_delegate_missionname_lb=tk.Label()
user_delegate_place_lb=tk.Label()
user_delegate_time_lb=tk.Label()
user_delegate_money_lb=tk.Label()
user_delegate_content_lb=tk.Label()

user_delegate_user_entry=tk.Entry()
user_delegate_missionname_entry=tk.Entry()
user_delegate_place_entry=tk.Entry()
user_delegate_time_entry=tk.Entry()
user_delegate_money_entry=tk.Entry()
user_delegate_content_text=tk.Text()

user_delegate_missionname=tk.StringVar()
user_delegate_place=tk.StringVar()
user_delegate_time=tk.StringVar()
user_delegate_money=tk.StringVar()
user_delegate_content=tk.StringVar()

user_delegate_backimg=tk.PhotoImage()
userdelegate_backbt=tk.Button()
user_delegate_sendimg=tk.PhotoImage()
userdelegate_sendbt=tk.Button()

#進入登入介面
setuserentrylayout()

def onclose():
    # clientsocket.send(DISCONNECT_MESSAGE.encode())
    # pygame.mixer.music.stop()
    window.destroy()

window.protocol("WM_DELETE_WINDOW",onclose)
window.mainloop()