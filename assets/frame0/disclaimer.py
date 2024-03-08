
from pathlib import Path
import psutil
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Label, Frame
import ctypes
import os
import shutil
from colored import fg, attr
from PIL import Image, ImageDraw, ImageSequence
import shutil
import matplotlib.font_manager as fm
import winsound
import subprocess
import requests
import psutil
from pathlib import Path
import winreg
import time
import uuid
from time import sleep
from colored import fg, attr
from termcolor import colored
import time
import matplotlib.pyplot as plt
from zipfile import ZipFile
from io import BytesIO
from packaging import version
import sys


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path("~").expanduser() / Path("AppData/Local/GreekProject/DoTLook-main/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("415x523")
window.configure(bg = "#FFFFFF")
window.title("GreekProject | Disclaimer")
window.resizable(False, False)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 523,
    width = 415,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_1 = canvas.create_image(
    213.0,
    287.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    bg="#d9d9d9",
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
button_1.place(
    x=310.0,
    y=472.0,
    width=90.3525390625,
    height=37.598533630371094
)
window.resizable(False, False)
window.mainloop()
