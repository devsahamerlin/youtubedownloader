from tkinter import *


def open_window():
    top = Toplevel()
    top.title("Youtube video downloader app")
    top.geometry("400x200")


    Label(top, text="Welcome to YouTube downloader app").pack()
    myVar = StringVar()
    myVar.set("Enter the link below")
    Entry(top, textvariable=myVar, width=40).pack(pady=10)
    link = StringVar()
    Entry(top, textvariable=link, width=40).pack(pady=10)
    Button(top, text="Donwload video", command=download).pack()

    button1 = Button(top, text="close", command=top.destroy)
    button1.pack()

def open_window2():
    top = Toplevel()
    top.title("mp3 Player")
    top.geometry("400x200")
    button1 = Button(top, text="close", command=top.destroy)
    button1.pack()


root = Tk()
button = Button(root, text="Download video", command=open_window)
button.pack()
button2 = Button(root, text="Audio player", command=open_window2)
button2.pack()

root.geometry("300x300+120+120")
root.title("Video et Mp3 App")
root.mainloop()
