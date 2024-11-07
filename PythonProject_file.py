def menu():
    print(".........................................................................")
    print("                       |         MENU          |                         ")
    print(".........................................................................")
    print("|     1     |     2     |     3     |     4     |     5     |     6     |")
    print(".........................................................................")
    print("|     7     |     8     |     9     |     10    |     11    |     12    |")
    print(".........................................................................")
    print("|     13    |     14    |     15    |     16    |     17    |     18    |")
    print(".........................................................................")
    print("|     19    |     20    |     21    |     22    |     23    |     24    |")
    print(".........................................................................")


# menu()
Q=[
    "Quelle est la capitale de la France ?",
    "Quel est le plus grand océan du monde ?",
    "Qui a écrit Roméo et Juliette ?",
    "Quel est l'élément chimique dont le symbole est O ?",
    "Quel est le pays d'origine du sushi ?",
    "Quel animal est connu comme le roi de la jungle ?",
    "Quelle planète est connue comme la planète rouge ?",
    "Qui a peint la Mona Lisa ?",
    "Quel est le plus long fleuve du monde ?",
    "Quel sport utilise un ballon ovale ?",
    ".................",
    "BOMM",

]
R1=["A- Berlin","A- Atlantique","A- Victor Hugo","A- Or","A- Chine","A- Tigre","A- Vénus","A- Vincent van Gogh","A- Amazone","A- Football","","you loss"]


R2=["B- Madrid","B- Indien","B- William Shakespeare","B- Oxygène","B- Japon","B- TLéopard","B- Mars","B- Pablo Picasso","B- Nil","B- Rugby","",""]


R3=["C- Paris","C- Pacifique","C- Molière","C- Hydrogène","C- Hydrogène","C- Corée","C- Lion","C- Léonard de Vinci","C- Yangtsé","C- Basketball","",""]


R4=["D- Rome","D- Arctique","D- Gustave Flaubert","D- Azote","D- Thaïlande","D- Éléphant","D- Saturne","D- Claude Monet","D- Mississippi","D- Tennis","",""]
VraiReponce=[] 
for i in range(1,12):
    print(Q[i])
    if R1[i] =="":

        pass
    else:
        print(" ",R1[i])
    
    if R2[i] =="":

        pass
    else:
        print(" ",R2[i])
    if R3[i] =="":

        pass
    else:
        print(" ",R3[i])
    if R4[i] =="":

        pass
    else:
        print(" ",R4[i])


