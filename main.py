import tkinter as tk
from tkinter import filedialog
import time
import pyautogui
import os
from pathlib import Path

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.flag = False
        self.directory = tk.Label(self, text="")
        self.directory.pack()
        self.button = tk.Button(text="Choose Directory to Save", height=3, width=20, command= self.getDirectory)
        self.button.pack()
        self.value = [i for i in range(1,10)]
        var = tk.Variable(value=self.value)
        self.listbox = tk.Listbox(listvariable=var,height=3,selectmode=tk.EXTENDED)
        self.listbox.pack()
        self.start = tk.Button(text="Start Capturing", height=3, width=20, command=self.start)
        self.start.pack()
        self.start = tk.Button(text="Stop Capturing", height=3, width=20, command=self.stop)
        self.start.pack()
        # start the clock "ticking"

    def getDirectory(self):
        self.folder_selected = filedialog.askdirectory()
        self.directory.config(text=self.folder_selected)

    def capture(self):
        now = time.strftime("%H:%M:%S" , time.gmtime())
        now = now.replace(':','-')
        selected=''
        for i in self.listbox.curselection():
            selected = self.listbox.get(i)
        if selected and self.directory.cget("text") != "":
            print("Capturing and saving image")
            timer=selected*1000*60
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(os.path.join(self.directory.cget("text") + '/' + now + '.png'))
            if self.flag is True:
                self.after(timer, self.capture)
                print("Wait for another capture")
            else:
                print("Capturing stopped")
        elif selected and self.directory.cget("text") == "":
            print("Please pick a directory")
        elif not selected and self.directory.cget("text") != "":
            print("Please pick the capture minutes")
        else:
            print("Please pick a directory and the capture minutes")

    def start(self):
        self.flag=True
        self.capture()
    def stop(self):
        self.flag=False

if __name__== "__main__":
    app = SampleApp()
    app.mainloop()