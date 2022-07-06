import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def Container():
 
    # Heading Section
    head_label = Label(root, text="YouTube Video Downloader", padx=15, pady=15, font="SegoeUI 14", fg="black")
    head_label.grid(row=1, column=1, pady=5, padx=5, columnspan=3)
 
    # URL Section
    link_label = Label(root, text="Enter URL :", pady=5, padx=5)
    link_label.grid(row=2, column=0, pady=5, padx=5)
 
    root.linkText = Entry(root, width=47, textvariable=video_Link, font="Arial 10")
    root.linkText.grid(row=2, column=1, ipady=5, ipadx=1, columnspan=2)
 
    # Save_To Section
    destination_label = Label(root, text="Save To :", pady=5, padx=5)
    destination_label.grid(row=3, column=0, pady=5, padx=1)
 
    root.destinationText = Entry(root, width=35, textvariable=download_Path, font="Arial 10")
    root.destinationText.grid(row=3, column=1, ipady=5, ipadx=10)
    
    # Browse Button
    browse_B = Button(root, text="Browse", command=Browse, width=5, bg="lightgray", relief=GROOVE)
    browse_B.grid(row=3, column=2, ipady=2, ipadx=10)
 
    # Download Button
    Download_B = Button(root, text="Download", command={'Download'}, width=10, bg="lightgray", relief=GROOVE, font="Arial 10")
    Download_B.grid(row=5, column=1, pady=5, padx=5, columnspan=3)
    
def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_Directory)
root = tk.Tk()
root.geometry("480x240")
root.resizable(False, False)
root.title("YouTube Video/Audio Downloader")

video_Link = StringVar()
download_Path = StringVar()
 

Container()
root.mainloop()
