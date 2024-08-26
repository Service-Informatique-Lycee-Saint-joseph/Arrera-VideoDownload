import customtkinter as ctk
from tkinter import*

class CArreraDGUI :
    def __init__(self) :
        self.__windows = ctk.CTk()
        self.__windows.title("Arrera Download")
        icon = PhotoImage(file="image/ArreraVideoDownload.png")
        self.__windows.iconphoto(False,icon)
        self.__windows.maxsize(500,500)
        self.__windows.minsize(500,500)
        
        labelTitle = ctk.CTkLabel(self.__windows,text="Arrera Download",font=("Arial",30))
        self.__entryURL = ctk.CTkEntry(self.__windows, placeholder_text="Entrez URL",font=("Arial",15),width=300)
        btnDownload = ctk.CTkButton(self.__windows,text ="Telecharger",font=("Arial",25))
        btnChooseFile = ctk.CTkButton(self.__windows,text ="Dossier Sortie",font=("Arial",25))
        
        labelTitle.pack()
        btnDownload.place(relx=1, rely=1, anchor='se')
        btnChooseFile.place(relx=0, rely=1, anchor='sw')
        self.__entryURL.place(relx=0.5, rely=0.3, anchor="center")
    
    def windows(self):
        self.__windows.mainloop()
        