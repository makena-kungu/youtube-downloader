import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import OptionMenu as oP

import main
from text_listener import *


def container():
    # Heading Section
    head_label = Label(_frame, text="YouTube Video Downloader", padx=15, pady=15, font="SegoeUI 12", fg="black",
                       wraplength=400)
    head_label.grid(row=1, column=0, pady=5, padx=5, columnspan=4, sticky=NSEW)

    # URL Section
    link_label = Label(_frame, text="Enter URL :", pady=5, padx=5)
    link_label.grid(row=2, column=0, columnspan=1, pady=5, padx=5)

    _frame.linkText = Entry(_frame, width=55, textvariable=video_Link, font="Arial 10")
    _frame.linkText.grid(row=2, column=1, ipady=5, ipadx=1, columnspan=3)
    _frame.linkText.grid(sticky=E)

    # Save_To Section
    destination_label = Label(_frame, text="Save To :", pady=5, padx=5)
    destination_label.grid(row=3, column=0, pady=5, padx=1)

    _frame.destination_text = Entry(_frame, width=42, textvariable=download_path, font="Arial 10")
    _frame.destination_text.grid(row=3, column=1, columnspan=2, ipady=5, ipadx=10, sticky=E)

    # Browse Button
    browse_button = Button(_frame, text="Browse", command=browse, width=5, bg="lightgray", relief=GROOVE)
    browse_button.grid(row=3, column=3, ipady=3, ipadx=10, sticky=E)

    # menu
    options_menu = oP(_frame, menu_var)
    options_menu.grid(row=4, column=1)

    # Download Button
    download_button = Button(_frame, text="Download", command=download, width=10, bg="lightgray", relief=GROOVE,
                             font="Arial 10")
    download_button.grid(row=4, column=2, pady=5, padx=5)

    # error label
    error_label.grid(row=5, column=0, columnspan=4, sticky=NSEW)

    # listen to text changes in the video link Entry widget
    attach_listener(video_Link, head_label, options_menu=options_menu, error_label=error_label)


def browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_path.set(download_directory)


def download():
    print('downloading')
    (msg, is_successful, path) = main.download(res=menu_var.get(), path=download_path.get(), video_url=video_Link.get())
    error_label.config(fg='green' if is_successful else 'red', text=msg)
    # open the directory where the file is downloaded
    os.system(r'start ' + download_path.get())
    print(msg)


root = tk.Tk()
# root.geometry("480x240")
root.resizable(False, False)

_frame = tk.Frame(root)
_frame.grid(column=0, row=0)

_frame.columnconfigure(0, weight=1)
_frame.grid_configure(padx=35, pady=20)
root.title("YouTube Video/Audio Downloader")

video_Link = StringVar()
menu_var = StringVar()
download_path = StringVar()

error_label = Label(_frame, pady=5, padx=5, font="Arial 10", fg='red', justify=CENTER)

container()
root.mainloop()
