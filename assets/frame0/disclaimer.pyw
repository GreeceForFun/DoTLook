import os
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_close():
    window.destroy()

if __name__ == "__main__":
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = Path("~").expanduser() / Path("AppData/Local/GreekProject/DoTLook-main/assets/frame0")

    icon_file_path = Path("~").expanduser() / Path("AppData/Local/GreekProject/DoTLook-main/assets/frame0/icon.ico")

    window = Tk()
    window.geometry("415x523")
    window.configure(bg="#FFFFFF")
    window.title("GreekProject | Disclaimer")
    window.resizable(False, False)
    window.iconbitmap(icon_file_path)

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=523,
        width=415,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_11.png"))
    image_1 = canvas.create_image(213.0, 287.0, image=image_image_1)

    button_image_1 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        bg="#d9d9d9",
        highlightthickness=0,
        command=on_close,
        relief="flat"
    )
    button_1.place(x=310.0, y=472.0, width=90.3525390625, height=37.598533630371094)

    window.protocol("WM_DELETE_WINDOW", on_close)  # Handle window close event
    window.mainloop()