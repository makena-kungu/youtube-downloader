from tkinter import StringVar, Label
from tkinter.ttk import OptionMenu

from pytube.exceptions import RegexMatchError

from main import *


def callback(link_var, head: Label, error_label: Label, options: OptionMenu):
    try:
        url = link_var.get()
        t = title(url)
        error_label.config(text='', fg='red')
        head.config(text=t)

        # get the resolutions
        resolutions = get_resolutions(url)

        menu_var = StringVar()
        menu_var.set(resolutions[len(resolutions) - 1])
        # clear items from the menu
        options.set_menu('720p', *resolutions)
    except RegexMatchError:
        text = 'Invalid URL!'
        error_label.config(text=text, fg='red')
        print(text)


def attach_listener(link_var: StringVar, header: Label, error_label: Label, options_menu: OptionMenu):
    link_var.trace("w", lambda *args: callback(link_var, header, error_label, options_menu))
    return link_var
