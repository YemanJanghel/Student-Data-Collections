from  tkinter import*
from tkinter import  messagebox
import mysql.connector


background="#06283D"
framebg="EDEDED"
framefg="#06283D"

root=Tk()
root.title("Login System")
root.geometry("1250x700")
root.config(bg=background)
root.resizable(False,False)

def register():
    username = user.get()
    password = code.get()
    admincode=adminaccess.get()
    #print(username,password,admincode)
    if admincode=="9955":
        if (username=="" or username=="UserID") or (password=="" or password=="Password"):
            messagebox.showerror("Enter error","Type username or password!!!")
        else:

            try:
                mydb = mysql.connector.connect(host='localhost', user='root', password='seedit')
                mycursor = mydb.cursor()
                print("Connection established!!!")
            except:
                messagebox.showerror("Connection", "Database connection not stablish!!")

            try:
                command="create database studentregistration"
                mycursor.execute(command)

                command = "use studentregistration"
                mycursor.execute(command)

                command = "create table login (user int auto_increment key not null, username varchar(50),Password varchar(100))"
                mycursor.execute(command)

            except:
                mycursor.execute("use studentregistration")
                mydb = mysql.connector.connect(host='localhost', user='root', password='seedit',db='studentregistration')
                mycursor = mydb.cursor()

                command="insert into login(Username,Password) values(%s,%s)"
                mycursor.execute(command,(username,password))
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Register","New User Added Successfully!!!!")


    else:
        messagebox.showerror("Admin code!!", "Input Correct Admin code to add new user!!")


def login():
    root.destroy()
    import login

#icone image
image_icone=PhotoImage(file="images/icon.png")
root.iconphoto(False,image_icone)

#background image
frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="images/register.png")
Label(frame,image=backgroundimage).pack()

adminaccess=Entry(frame,width=15,fg="#000",border=0,bg="#e8ecf7",font=("Arial Bold",20),show="*")
adminaccess.focus()
adminaccess.place(x=550,y=280)

########user entry
def user_enter(e):
    user.delete(0,'end')

def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,"UserID")

user =Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=("Arial Bold",24))
user.insert(0,"UserID")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500,y=380)


########password entry
def password_enter(e):
    code.delete(0,'end')

def password_leave(e):
    if code.get()=='':
        user.insert(0,"Password")

code =Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=("Arial Bold",24))
code.insert(0,"Password")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=500,y=470)


######################################################################################
button_mode=True

def hide():
    global button_mode

    if button_mode:
        eyeButton.config(image=closeeye,activebackground="white")
        code.config(show="*")
        button_mode=False
    else:
        eyeButton.config(image=openeye, activebackground="white")
        code.config(show="")
        button_mode =True

openeye=PhotoImage(file="Images/openeye.png")
closeeye=PhotoImage(file="Images/close eye.png")
eyeButton=Button(frame,image=openeye,bg="#375174",bd=0,command=hide)
eyeButton.place(x=780,y=470)


#################################################################################33

regis_Button=Button(root,text="ADD NEW USER",bg="#455c88",fg="white",width=13,height=1,font=("Arial",16,"bold"),bd=0,command=register)
regis_Button.place(x=530,y=600)

backbuttonimage=PhotoImage(file="Images/backbutton.png")
Backbuttonimage=Button(root,image=backbuttonimage,fg="#deeefb",command=login)
Backbuttonimage.place(x=20,y=15)


root.mainloop()