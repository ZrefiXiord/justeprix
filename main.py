from tkinter import *
from tkinter import messagebox
from math import *
from random import *
import time
import datetime


Fenetre = Tk()
Fenetre.title('Le juste prix')
Fenetre.geometry('300x100+400+400')

t0=0
joueur=0
nombre=randint(1,1000)




t0=time.time()




def reset():
    global nombre, joueur, t0
    nombre=randint(1,1000)
    joueur=0
    t0=time.time()
    value_label.set("Dites un nombre entre 1 et 1000")
    value_edit.set("")
    temps.set("")


def svg():
    global joueur, nombre, t0
    joueur = value_edit.get()
    if int(joueur)<1 or int(joueur)>1000:
        messagebox.showerror('Erreur', 'Veuillez saisir un nombre en 1 et 1000')
    if int(joueur) > nombre:
        value_label.set("Plus petit")
    elif int(joueur) < nombre:
        value_label.set("Plus grand")
    else:
        ttotal=time.time() - t0
        value_label.set("Gagné")
        temps.set(str(datetime.timedelta(seconds=ttotal)))
        if messagebox.askyesno('Rejouer', 'Voulez vous rejouer?') == 0:
            Fenetre.destroy()
        else:
            reset()

value_edit = StringVar()

value_label = StringVar()
value_label.set("Dites un nombre entre 1 et 1000")
temps= StringVar()
temps.set("")
entree = Entry(Fenetre, textvariable=value_edit, width=30)
entree.place(x=20, y=10, width=100, height=25)




LabelResultat = Label(Fenetre, textvariable  = value_label, fg ='red')
LabelResultat.place(x=20, y=40, width=225, height=25)
TempsR = Label(Fenetre, textvariable = temps, fg='blue')
TempsR.place(x=20, y=65, width=225, height=25)
BoutonSave = Button(Fenetre, text ='Confirmer', command = svg)
BoutonSave.place(x=130, y=10, width=100, height=25)




Fenetre.mainloop()
