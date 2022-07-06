from tkinter import StringVar, Label, Tk, Menu
from tkinter.ttk import OptionMenu, Entry

from pytube.exceptions import RegexMatchError

from main import *


def callback(sv, head: Label, options: OptionMenu):
    try:
        url = sv.get()
        t = title(url)
        print(t)
        head.config(text=t)

        # get the resolutions
        ress = get_resolutions(url)
        menu_var = StringVar()
        menu_var.set(ress[len(ress) - 1])
        # clear items from the menu
        options.set_menu('720p', *ress)
    except RegexMatchError:
        pass


def attach_listener(sv: StringVar, header: Label, drop_down: OptionMenu):
    sv.trace("w", lambda *args: callback(sv, header, drop_down))
    return sv
