from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

window=Tk()
window.title("Text to speech")
window.geometry("900x450+300+100")
window.resizable(False,False)
window.configure(bg="#305065")

engine = pyttsx3.init()

def img(name):
    return os.path.join(BASE_DIR, "images", name)

def speak_now():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def set_voice():
        if gender == 'Male':
            engine.setProperty('voice', voices[1].id)
        elif gender == 'Greek':
            engine.setProperty('voice', voices[4].id)
        else:
            engine.setProperty('voice', voices[2].id)
        engine.say(text)
        engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == "Normal":
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate',60)
        set_voice()


def downloads():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def set_voice():
        if gender == 'Male':
            engine.setProperty('voice', voices[1].id)
        elif gender == 'Greek':
            engine.setProperty('voice', voices[4].id)
        else:
            engine.setProperty('voice', voices[2].id)

        path = filedialog.askdirectory()
        os.chdir(path)
        engine.save_to_file(text, 'text.mp3')
        engine.runAndWait()

    if text:
        if speed == "Normal":
            engine.setProperty('rate', 250)
        elif speed == "Normal":
            engine.setProperty('rate', 250)
        else:
            engine.setProperty('rate', 60)

        set_voice()

Top_frame=Frame(window,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo = PhotoImage(file=img("speaker_logo.png"))
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)

Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=35)


text_area=Text(window,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(window,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)

Label(window,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)


gender_combobox=Combobox(window,values=['Male','Greek','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(window,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

speak_icon = PhotoImage(file=img("speak.png"))
btn=Button(window,text="speak",image=speak_icon,width=130,font="arial 14 bold",command=speak_now)
btn.place(x=550,y=280)

download_icon = PhotoImage(file=img("download.png"))
save=Button(window,text="Save",image=download_icon,width=130,bg="#39c790",font="arial 14 bold",command=downloads)
save.place(x=730,y=280)

window.iconphoto(False,speak_icon)

window.mainloop()
