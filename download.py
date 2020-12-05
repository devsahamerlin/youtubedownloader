from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("400x200")

root.title("Youtube video downloader app")

def download():
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video downloaded successfuly")
    except Exception as e:
        myVar.set("Error")
        root.update()
        link.set("Enter correct link")


Label(root, text="Welcome to YouTube downloader app").pack()
myVar = StringVar()
myVar.set("Enter the link below")
Entry(root, textvariable=myVar, width=40).pack(pady=10)
link = StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)
Button(root, text="Donwload video", command=download).pack()

root.mainloop()
