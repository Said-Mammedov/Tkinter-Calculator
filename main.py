from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("1920x1080")
window.resizable(True, True)
window.iconbitmap("M.ico")
window.title("MyStat")

image = Image.open("image.png")
image = image.resize((1050,1080))
photo = ImageTk.PhotoImage(image)
foto = Label( window, image=photo )
foto.place(x= 855, y= 0)


def register():
    window.destroy()


mystat = Label(window,text ="MyStat",fg="blue",font=("Arial", 30, "bold"))
mystat.place(x=20, y = 20 )

login_label = Label(window,text ="Login",fg="black",font=("Arial", 20, "bold"))
login_label.place(x = 430, y= 380)

login_entry = Entry(window, fg= "gray", width=20,font=("Arial", 25, "bold"))
login_entry.insert(0,"Login*")
login_entry.place(x=300, y= 450)

password_entry = Entry(window, fg= "gray", width=20,font=("Arial", 25, "bold"), show="*")
password_entry.place(x=300, y= 550)

login_btn = Button(window, text="Login", bg="purple", fg="white",
                   width=18, font=("Arial", 25, "bold"),
                   command=register)

login_btn.place(x=300, y=650)




mainloop()