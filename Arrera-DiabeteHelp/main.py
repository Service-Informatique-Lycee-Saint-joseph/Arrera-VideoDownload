from tkinter import*
import webbrowser

Navigateur =  "/usr/bin/firefox"
color ="white"
textcolor = "black"

def CalendrierDia():
    webbrowser.get(Navigateur).open("https://calendar.google.com/calendar/u/0/gp?hl=fr")
def MAJcapt():
    webbrowser.get(Navigateur).open("https://www.freestylediabete.fr/maj-firmware")
def note():
    webbrowser.get(Navigateur).open("https://www.notion.so/Note-utile-2c163bc4b80c4b76ade427b527ab5704")
def insuline():
    webbrowser.get(Navigateur).open("https://www.notion.so/689dbc0bafea401b9127d72512fd6057?v=a9585f80d1ac4faa8785b21cf18b897a")
def repas():
    webbrowser.get(Navigateur).open("https://www.notion.so/Historique-des-repas-dfd8ab2629dd467c9ab13377dbd64e16")

screen = Tk()
screen.title("Arrera : Diabete Help")
screen.maxsize(300,250)
screen.minsize(300,250)
screen.wait_visibility(screen)
screen.wm_attributes('-alpha',1)
screen.config(bg=color)
#cadre
Cadre1 = Frame(screen,bg=color,width=10)
Cadre2 = Frame(screen,bg=color)
#bouton
BoutonInsuline = Button(screen,text="Dose d'Insuline",bg=color,fg=textcolor)

BoutonRepas = Button(Cadre1,text="Repas",bg=color)
IconRepas=PhotoImage(master=BoutonRepas,file="image/IconRepas.png")
BoutonRepas.image_names=IconRepas
BoutonRepas.config(image=IconRepas,command=repas)

BoutonCalendrier = Button(Cadre1,text="Calendrier Capteur",bg=color)
IconCallendrier = PhotoImage(master=BoutonCalendrier,file="image/IconCalendrier.png")
BoutonCalendrier.image_names=IconCallendrier
BoutonCalendrier.config(image=IconCallendrier,command=CalendrierDia)

BoutonAbbote = Button(Cadre2,text="abbote",bg=color)
IconAbotte = PhotoImage(master=BoutonAbbote,file="image/IconAbotte.png")
BoutonAbbote.image_names = IconAbotte
BoutonAbbote.config(image=IconAbotte,command=MAJcapt)

BoutonNote = Button(Cadre2,text="Note",bg=color)
IconNote = PhotoImage(master=BoutonNote,file="image/IconNote.png")
BoutonNote.image_names = IconNote
BoutonNote.config(image=IconNote,command=note)

BoutonLibreview = Button(screen,text="Libreview",bg=color,fg=textcolor)
    
#label
Label1=Label(Cadre1,bg=color,width=6)
Label2=Label(Cadre1,bg=color,width=6)
Label3=Label(Cadre2,bg=color,width=6)
Label4=Label(Cadre2,bg=color,width=6)
Label5=Label(screen,height=2,bg=color)
#affichage 
Cadre1.pack()
Label5.pack()
Cadre2.pack()
BoutonInsuline.pack(side="left",anchor="s")
BoutonLibreview.pack(side="right",anchor="s")
    
BoutonCalendrier.pack(side="left")
Label2.pack(side="left")
BoutonRepas.pack(side="right")
Label1.pack(side="right")
    
BoutonAbbote.pack(side="right")
Label3.pack(side="right")
BoutonNote.pack(side="left")
Label4.pack(side="left")
screen.mainloop()