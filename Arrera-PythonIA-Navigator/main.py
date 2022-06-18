from tkinter import*
import subprocess
import os

screen = Tk()
def Jupyter():
    os.popen("jupyter notebook")
def Spyder():
    os.popen("/usr/bin/spyder")
screen.title("Arrera IA Navigator")
screen.iconphoto(False,PhotoImage(file="image/Icon.png"))
screen.maxsize(700,250)
screen.minsize(700,250)
screen.config(bg="white")

Label1 = Label(screen,bg="white",width=20)
Label2 = Label(screen,bg="white",width=20)

BoutonSpyder = Button(screen,text="S",command=Spyder,bg="white")
BoutonJypiter = Button(screen,text="J",command=Jupyter,bg="white")

IconSpyder = PhotoImage(file="image/IconSpyder.png",master=BoutonSpyder)
IconJupyter = PhotoImage(file="image/IconJupyter.png",master=BoutonSpyder)

BoutonSpyder.image_names = IconSpyder
BoutonJypiter.image_names = IconJupyter

BoutonSpyder.config(image=IconSpyder)
BoutonJypiter.config(image=IconJupyter)

Label1.pack(side="left")
BoutonSpyder.pack(side="left")

Label2.pack(side="right")
BoutonJypiter.pack(side="right")

screen.mainloop()