import sys
from imageio import imread
from time import sleep
from os import name, system
from os.path import join, dirname, abspath
from matplotlib.pyplot import imshow, show
from webbrowser import open_new
from tkinter import Tk
from tkinter.filedialog import askdirectory
from shutil import copy

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    is_exe = True
    bundle_dir = getattr(
        sys, '_MEIPASS', abspath(
            dirname(__file__)))
    path_to_res = join(bundle_dir, 'res')
else:
    is_exe = False
    path_to_res = join(dirname(__file__), 'res')


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if name == 'posix':
        _ = system('clear')
    else:
        # for windows platfrom
        _ = system('cls')


def timed_print(msg: str, secs: int):
    print(msg, end="", flush=True)
    for _ in range(secs):
        sleep(1)
        print(".", end="", flush=True)
    print()


def im_show(filename: str):
    filepath = join(path_to_res, filename)
    fig = imshow(imread(filepath))
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig.axes.margins(0, tight=None)
    show()


def copyFile(filename):
    tkroot = Tk()
    tkroot.lift()
    tkroot.attributes('-topmost', True)
    tkroot.withdraw()
    dst = askdirectory()
    print("Copied to ", dst)
    src = join(path_to_res, filename)
    tkroot.destroy()
    try:
        _ = copy(src, dst)
        return dst
    except Exception as e:
        print(e)
        return False


def close_game():
    if is_exe:
        sys.exit(0)
    else:
        exit()


def opensite(sitename):
    open_new("file://" + join(path_to_res, sitename))
