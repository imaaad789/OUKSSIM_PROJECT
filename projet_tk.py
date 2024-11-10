from tkinter import *
from PIL import Image, ImageTk


import csv
with open("infopersonnelle.csv", "w", newline='', encoding='utf-8') as ficher:
    con=csv.writer(ficher,delimiter=";")
    con.writerow(["Nom","Prenom","CIN","Date de naissance","Adress","Email","Note1","Note2","Moyenne","Mention"])

def fichercsv(Liste_donnee):
    import csv
    with open("infopersonnelle.csv", "a", newline='', encoding='utf-8') as ficher:
        con=csv.writer(ficher,delimiter=";")
        con.writerow(Liste_donnee)    

def afficheficher():
    import csv
    with open("ficher.csv", "r", newline='', encoding='utf-8') as ficher:
        con=csv.reader(ficher,delimiter=";")
        print("Les résultats final de chaque groupe :  ")
        for i in con:
            print(i)

def moyenne(not1,not2):
    return (not1+not2)/2

def mention(moy):
    if moy>16:
        return("T.bien")
    if (moy<16 and moy>=14):
        return("bien")
    if (moy<14 and moy>=12):
        return("A.bien")
    if (moy<12 and moy>=10):
        return("passable")
    if moy<10:
        return("reoudeblemment")


Liste=[]
def save():
    nom=T1.get()
    prenom=T2.get()
    adress=T3.get()
    email=T4.get()
    note1=float(T5.get())
    note2=float(T6.get())
    CIN=T7.get()
    date_naissance=T8.get()
    moyen=moyenne(note1,note2)
    ment=mention(moyen)
    Liste.append((nom,prenom,CIN,date_naissance,adress,email,note1,note2,moyen,ment))
    fichercsv(Liste)

# def Initialisation():  
#     N.set("")
#     P.set("")
#     ad.set("")
#     em.set("")
#     n1.set(0)
#     n2.set(0)
#     cin.set("")
#     dn.set("")


fenetre=Tk()
fenetre.geometry("1050x600")


fenetre.title("picture")
original_img = Image.open("C:/Users/L/Desktop/python/projet_tk/crown-gold.png")
img = ImageTk.PhotoImage(original_img)
label = Label(fenetre, image=img,width=150,height=150)
label.place(x=850, y=10)

labinfo=Label(fenetre,text="Information personnelle", font="sans-serif, 14 bold")
labinfo.place(x=450,y=20)

lab1=Label(fenetre,text="Nom: ", font="sans-serif, 12 bold")
lab1.place(x=50,y=150)
# N=StringVar()
T1=Entry(fenetre)
T1.place(x=250,y=150,height="18px", width="200px")



lab1=Label(fenetre,text="Prenom: ", font="sans-serif, 12 bold")
lab1.place(x=50,y=200)
# P=StringVar()
T2=Entry(fenetre)
T2.place(x=250,y=200,height="18px", width="200px")


# -------adress
lab1=Label(fenetre,text="Adress: ", font="sans-serif, 12 bold")
lab1.place(x=590,y=150)
# ad=StringVar()
T3=Entry(fenetre)
T3.place(x=700,y=150,height="18px", width="200px")


# ----------email
lab1=Label(fenetre,text="Email: ", font="sans-serif, 12 bold")
lab1.place(x=590,y=200)
# em=StringVar()
T4=Entry(fenetre)
T4.place(x=700,y=200,height="18px", width="200px")


# -------note1
lab1=Label(fenetre,text="Note1: ", font="sans-serif, 12 bold")
lab1.place(x=590,y=250)
# n1=IntVar()
T5=Entry(fenetre)
T5.place(x=700,y=250,height="18px", width="200px")


# ----------note2
lab1=Label(fenetre,text="Note2: ", font="sans-serif, 12 bold")
lab1.place(x=590,y=300)
# n2=IntVar()
T6=Entry(fenetre)
T6.place(x=700,y=300,height="18px", width="200px")


lab1=Label(fenetre,text="CIN: ", font="sans-serif, 12 bold")
lab1.place(x=50,y=250)
# cin=StringVar()
T7=Entry(fenetre)
T7.place(x=250,y=250,height="18px", width="200px")


lab1=Label(fenetre,text="Date de naissance: ", font="sans-serif, 12 bold")
lab1.place(x=50,y=300)
# dn=StringVar()
T8=Entry(fenetre)
T8.place(x=250,y=300,height="18px", width="200px")



save_bouton = Button( fenetre , text ="Save" , command=save, bg="silver", font="sans-serif, 12 bold")
save_bouton.place(x=200,y=350)

initialisation_bouton = Button( fenetre , text ="Initialisation" , command=quit , bg="silver", font="sans-serif, 12 bold")
initialisation_bouton.place(x=300,y=350)

affiche_bouton = Button( fenetre , text ="Affiche" , command=afficheficher , bg="silver", font="sans-serif, 12 bold")
affiche_bouton.place(x=450,y=350)

modifier_bouton = Button( fenetre , text ="Modifier" , command=quit , bg="silver", font="sans-serif, 12 bold")
modifier_bouton.place(x=550,y=350)

quitte_bouton = Button( fenetre , text ="Quitte" , command=quit , bg="silver", font="sans-serif, 12 bold")
quitte_bouton.place(x=650,y=350)






fenetre.mainloop()
