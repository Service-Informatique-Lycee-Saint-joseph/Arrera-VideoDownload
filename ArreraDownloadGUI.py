import customtkinter as ctk
from tkinter import*
from ArreraDownload import*
from tkinter.messagebox import*
from travailJSON import*

class CArreraDGUI :
    def __init__(self) :
        self.__windows = ctk.CTk()
        self.__windows.title("Arrera Download")
        icon = PhotoImage(file="image/ArreraVideoDownload.png")
        self.__windows.iconphoto(False,icon)
        self.__windows.maxsize(500,500)
        self.__windows.minsize(500,500)
        self.__windows.iconbitmap("image/ArreraVideoDownload.ico")
        
        labelTitle = ctk.CTkLabel(self.__windows,text="Arrera Download",font=("Arial",30))
        self.__entryURL = ctk.CTkEntry(self.__windows, placeholder_text="Entrez URL",font=("Arial",15),width=300)
        btnDownload = ctk.CTkButton(self.__windows,text ="Telecharger",font=("Arial",25),command=self.__download)
        btnChooseFile = ctk.CTkButton(self.__windows,text ="Dossier Sortie",font=("Arial",25),command=self.__setFolder)
        
        labelTitle.pack()
        btnDownload.place(relx=1, rely=1, anchor='se')
        btnChooseFile.place(relx=0, rely=1, anchor='sw')
        self.__entryURL.place(relx=0.5, rely=0.3, anchor="center")
        
        # Mise en place de objet 
        self.__objetArrera = CArreraDownload()
        self.__jsonSetting = jsonWork("download.json")
    
    def active(self):
        self.__windows.mainloop()
    
    def __download(self):
        folder = self.__jsonSetting.lectureJSON("folder")
        if (folder == ""):
            self.__objetArrera.setDownloadFolder()
        else :
            self.__objetArrera.setDownloadFolderDur(folder)
        
        self.__objetArrera.setURL(self.__entryURL.get())
        
        self.__entryURL.delete(0,END)
        
        sortie = self.__objetArrera.download()
        
        if (sortie == True):
            showinfo("Download","Video telecharger")
        else :
            showerror("Download","Erreur de telechargement")
    
    def __setFolder(self):
        folder = filedialog.askdirectory(title="Dossier de telechargement")
        if (folder != "") :
            self.__jsonSetting.EcritureJSON("folder",folder)
            showinfo("Download","Dossier enregistrer")
        else :
            showerror("Download","Aucun dossier selectionner")