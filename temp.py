#imports
import tkinter 
import pytube

from tkinter import *

#root
root = Tk()
url = StringVar()

#top bar
canvas = Canvas(root, width=495, height=60, bg= '#010a14', bd=0)
canvas.pack(expand=True)
canvas.place(y=0,x=0)
#top bar text
toptxt = Label(root, text='YouTube To MP4 Converter', bg= '#010a14', fg='white')
toptxt.place(x=180,y=24)
#top image
topphoto = PhotoImage( file=r'D:\Coding\Python\youtube o mp4 converter\images\YouTube2.png')
#top image place
topphotolbl = Label(root, image=topphoto,)
topphotolbl.place(x=180,y=80)
#text box
txtfld = Entry(root, bg='#010a14', fg='#0f70d2', textvariable=url)
txtfld.place(x=180,y=300)
#button
btn = Button(root, text='Comfirm URL', bg='#010a14', fg='#0f70d2', command=lambda:[funcA(), funcB()])
btn.place(x=200,y=400)

def funcA():
    url.get()

def funcB():
    root.destroy()

root.title('nice')
root.geometry('500x500')
root.config(bg='#0f70d2')
root.mainloop()

from pytube import YouTube

url = url.get()

pytube.YouTube(url).streams.get_highest_resolution().download('/Videos')
