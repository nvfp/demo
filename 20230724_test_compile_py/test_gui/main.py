import base64

your_code = base64.b64encode(b"""

import os
import tkinter as tk
import subprocess as sp


DIR = os.path.dirname(os.path.abspath(__file__))
DEPENDENCY = os.path.join(DIR, 'dependencies', 'mytestapp.exe')


def main():

    root = tk.Tk()
    root.title('')
    root.iconbitmap(None)
    root.geometry('355x230+30+30')
    root.configure(bg='#111')

    # p = sp.run([DEPENDENCY], capture_output=True, text=True)
    # text = p.stdout.strip()
    text = 'abcdefg'
    # print(text)
    # print(repr(text))

    label = tk.Label(root, text=text)
    label.place(x=50, y=50, anchor='w')

    root.mainloop()


if __name__ == '__main__':
    main()
""")

exec(base64.b64decode(your_code))