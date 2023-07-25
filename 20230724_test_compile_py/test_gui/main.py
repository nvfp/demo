# import random
# import string
# def generate_random_hex():
#     hex_chars = string.hexdigits[:-6]  # Excludes 'abcdef' to ensure uppercase letters are included
#     random_hex = ''.join(random.choice(hex_chars) for _ in range(17))
#     return random_hex
# random_hex_string = generate_random_hex()
# print(random_hex_string)






import base64

your_code = base64.b64encode(b"""

import os
import tkinter as tk
import subprocess as sp
from tkinter import filedialog


FFMPEG_DIR = os.path.join(os.getenv('APPDATA'), 'FFMPEG_4596334371714dd94')
FFMPEG_BIN = os.path.join(os.getenv('APPDATA'), 'FFMPEG_4596334371714dd94', 'ffmpeg.exe')
FFPROBE_BIN = os.path.join(os.getenv('APPDATA'), 'FFMPEG_4596334371714dd94', 'ffprobe.exe')


def main():

    root = tk.Tk()
    root.title('')
    root.iconbitmap(None)
    root.geometry('355x230+30+30')
    root.configure(bg='#111')

    p = sp.run([DEPENDENCY], capture_output=True, text=True)
    text = p.stdout.strip()
    # print(text)
    # print(repr(text))

    label = tk.Label(root, text=text)
    label.place(x=50, y=50, anchor='w')

    root.mainloop()


if __name__ == '__main__':
    main()
""")

exec(base64.b64decode(your_code))