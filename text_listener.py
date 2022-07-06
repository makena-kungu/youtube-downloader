from tkinter import StringVar, Label, Tk, Menu
from tkinter.ttk import OptionMenu

from pytube.exceptions import RegexMatchError

from main import *


def callback(sv, head: Label, options: OptionMenu):
    try:
        url = sv.get()
        head.config(text=title(url))

        # get the resolutions
        ress = get_resolutions(url)
        menu_var = StringVar()
        menu_var.set(ress[len(ress) - 1])
        # clear items from the menu
        options.set_menu('720p', *ress)
    except RegexMatchError:
        pass


def attach_listener(widget: Label, drop_down: OptionMenu):
    sv = StringVar()

    sv.trace("w", lambda *args: callback(sv, widget, drop_down))
    return sv
