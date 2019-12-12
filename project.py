from tkinter import *
import sys
sys.path.insert(0,'package')
import requests

def internet_check():
    try:
        this = bool(requests.get("http://google.com"))
        return True
    except:
        online_btn.config(state="disabled", bg="red")


def online():
    root.destroy()
    import project_prototypeWithUI as online

def offline():
    root.destroy()
    import project_prototypeWithUI_Excel as offline

root = Tk()
root.minsize(400, 200)
root.maxsize(400, 200)

intro = Label(text="Please select mode", font=("AngsanaUPC", 24))
online_btn = Button(text="Online", command=online, bd=3, bg="lime")
online_txt = Label(text="Select this if you have internet connection")
offline_btn = Button(text="Offline", command=offline, bd=3, bg="aqua")
offline_txt = Label(text="Select this if you have no internet connection")
offline_btn
internet_check()
intro.pack()
online_txt.pack()
online_btn.pack()
offline_txt.pack()
offline_btn.pack()


root.mainloop()