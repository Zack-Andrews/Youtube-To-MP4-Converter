import tkinter
import pytube

from tkinter import *
root = Tk()
url = StringVar()
info = Label(root, text='youtube to mp4 converter')
info.place(x=60, y=50)
Enter = Button(root, text='Enter', command=lambda:[funcA(), funcB()])
Enter.place(x=100, y=80)
text = Entry(root, text='Url', textvariable=url)
text.place(x=60, y=120)

def funcA():
    url.get()
def funcB():
    root.destroy()

root.title('Calculator?')
root.geometry("300x200+10+10")
root.mainloop()

from pytube import YouTube

url = url.get()

pytube.YouTube(url).streams.get_highest_resolution().download('~/Downloads')


