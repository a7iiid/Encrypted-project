import keyboard
import pyperclip
from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        messagebox.showinfo(title="decrypt", message=decrypt)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("encryption", "Invalid Password")

def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.iconphoto(False, PhotoImage(file=r"C:\Users\ahm13\PycharmProjects\Project\images.ico"))

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="black", highlightbackground="#ed5533").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 10", bg="white",  bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("encryption", "Invalid Password")

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.iconphoto(False, PhotoImage(file=r"C:\Users\ahm13\PycharmProjects\Project\images.ico"))
    screen.title("Project")

    def reset():
        code.set("")
        text1.delete(1.0, END)


    global alt_pressed
    alt_pressed = True
    global ctrl_pressed
    ctrl_pressed = True
    def handle_paste(e):
        global alt_pressed

        if e.event_type == keyboard.KEY_DOWN and e.name == 'alt':
            if alt_pressed:
                text1.delete(1.0, END)
                text1.insert(END, pyperclip.paste())
                decrypt()




    def handle_copy(e):
        global ctrl_pressed

        if e.event_type == keyboard.KEY_DOWN and e.name == 'ctrl':
            if ctrl_pressed:
                pyperclip.copy("")
                keyboard.press_and_release("ctrl+c")





    Label(text="Enter text for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 20", bg="white",  bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)


    keyboard.on_press(handle_paste)
    keyboard.on_press(handle_copy)

    screen.mainloop()

main_screen()
