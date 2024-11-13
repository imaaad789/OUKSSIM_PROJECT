
import csv
import random

# Variables pour les donners de chaque groupe
score_groups = {
    1: {"Nom_grp":'',"membres":0,"correct": 0, "incorrect": 0, "bomb": 0, "score": 0, "win/loss": '', "classement": 0},
    2: {"Nom_grp":'',"membres":0,"correct": 0, "incorrect": 0, "bomb": 0, "score": 0, "win/loss": '', "classement": 0},
    3: {"Nom_grp":'',"membres":0,"correct": 0, "incorrect": 0, "bomb": 0, "score": 0, "win/loss": '', "classement": 0},
    4: {"Nom_grp":'',"membres":0,"correct": 0, "incorrect": 0, "bomb": 0, "score": 0, "win/loss": '', "classement": 0},
}
nombres_choisis=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
#fonction pour Le menu
def menu():
    print("-----------------------------------MENU----------------------------------\n"
          "|   01   |   02   |   03   |   04   |   05   |   06   |   07   |   08   |\n"
          "-------------------------------------------------------------------------\n"
          "|   09   |   10   |   11   |   12   |   13   |   14   |   15   |   16   |\n"
          "-------------------------------------------------------------------------\n"
          "|   17   |   18   |   19   |   20   |   21   |   22   |   23   |   24   |\n"
          "-------------------------------------------------------------------------\n"
    )

#Fonction pour le remplissage des fichiers
def qst_rpns():
    # ouverture du fichier des questions en ecriture pour le remplissage
    with open("QST.csv", "w", newline="", encoding="utf-8") as fQ:
        QST = csv.writer(fQ, delimiter=";")
        QST.writerow(["Quel est le plus grand ocean du monde?", "A)  Atlantique", "B)  Indien", "C)  Arctique ","D)  Pacifique"])
        QST.writerow(["Quel pays est connu pour la Tour Eiffel? ", "A)  Italie", "B)  Espagne", "C)  France","D)  Allemagne"])
        QST.writerow(["BOOM"])
        QST.writerow(["Quelle est la formule chimique de l'eau?", "A)  H2O", "B)  CO2", "C)  O2", "D)  H2SO4"])
        QST.writerow(["Combien y a-t-il de planetes dans notre systeme solaire?", "A)  7", "B)  8", "C)  9", "D)  10"])
        QST.writerow(["Qui a ecrit L'Origine des especes?", "A)  Isaac Newton", "B)  Albert Einstein", "C)  Charles Darwin","D)  Galilee"])
        QST.writerow(["Qui a remporté la Coupe du Monde de football en 2018 ?","A) Brésil","B) France","C) Allemagne","D) Argentine"])
        QST.writerow(["Quel animal est le plus rapide du monde ?","A) Guépard","B) Faucon pèlerin","C) Lion","D) Antilope"])
        QST.writerow(["BOOM"])
        QST.writerow(["En quelle année a été lancé le premier iPhone ?","A) 2005","B) 2007","C) 2009","D) 2010"])
        QST.writerow(["BOOM"])
        QST.writerow(["Quel langage de programmation est principalement utilisé pour développer des applications Android ?","A) Swift","B) JavaScript","C) Java","D) C"])
        QST.writerow(["Quel est le principal langage de programmation pour le développement de sites web côté client ?","A) C++","B) Python","C) Java","D) JavaScript"])
        QST.writerow(["BOOM"])
        QST.writerow(["Dans le domaine des réseaux, que signifie l'acronyme (DNS) ?","A) Digital Network System","B) Domain Network Service","C) Domain Name System","D) Data Network Service"])
        QST.writerow(["Quelle entreprise a développé le premier microprocesseur au monde, le 4004, en 1971 ?","A) AMD","B) Intel","C) IBM","D) Texas Instruments"])
        QST.writerow(["Quelle fonction Python est utilisée pour obtenir la longueur d’une liste ?","A) count()","B) length()","C) len()","D) size()"])
        QST.writerow(["Que fait la méthode pop() dans une liste en Python ?","A) Supprime tous les éléments de la liste","B) Supprime le dernier élément de la liste","C) Supprime un élément spécifique de la liste","D) Ajoute un élément en fin de liste"])
        QST.writerow(["Qui est la première femme élue présidente d’un pays africain ?","A) Ellen Johnson Sirleaf (Liberia)","B) Winnie Mandela (Afrique du Sud)","C) Joyce Banda (Malawi)","D) Ameenah Gurib-Fakim (Maurice)"])
        QST.writerow(["Quelle est la valeur de 81**1/2 ?","A) 9","B) 8","C) 7","D) 6"])
        QST.writerow(["Quel est le résultat de l’opération 7**2-6x5 ?","A) 9","B) 19","C) 29","D) 39"])
        QST.writerow(["Un objet de 2 kg est soumis à une force de 10 N. Quelle est son accélération ?","A) 8 m/s**2","B) 5 m/s**2","C) 15 m/s**2","D) 20 m/s**2"])
        QST.writerow(["Lorsqu’une onde se propage dans un milieu, elle transporte principalement ?","A) De la matière","B) De la lumière","C) De l'énergie","D) De la chaleur"])
        QST.writerow(["Quelle est la solution de l'inéquation 3x-5 < 10 ?","A) x<5","B) x>5","C) x>15","D) x<15"])
        QST.writerow(["En quelle année l'homme a-t-il marché sur la Lune pour la première fois ?","A) 1965","B) 1967","C) 1969","D) 1971"])
    # ouverture du fichier des reponses en ecriture pour le remplissage
    with open("reponse.csv", "w", newline="", encoding="utf-8") as fR:
        reponse = csv.writer(fR, delimiter=";")
        reponse.writerow(["Pacifique", ])
        reponse.writerow(["France"])
        reponse.writerow([""])
        reponse.writerow(["H2O"])
        reponse.writerow(["8"])
        reponse.writerow(["Charles Darwin"])
        reponse.writerow(["France"])
        reponse.writerow(["Faucon pèlerin"])
        reponse.writerow([""])
        reponse.writerow(["2007"])
        reponse.writerow([""])
        reponse.writerow(["Java"])
        reponse.writerow(["JavaScript"])
        reponse.writerow([""])
        reponse.writerow(["Domain Name System"])
        reponse.writerow(["Intel"])
        reponse.writerow(["len()"])
        reponse.writerow(["Supprime le dernier élément de la liste"])
        reponse.writerow(["Ellen Johnson Sirleaf (Liberia)"])
        reponse.writerow(["9"])
        reponse.writerow(["9"])
        reponse.writerow(["5 m/s**2"])
        reponse.writerow(["De l'énergie"])
        reponse.writerow(["x<5"])
        reponse.writerow(["1969"])

# ouverture du fichier des donners
def open_lire_ficher():
    with open("donner.csv", "w", newline='', encoding='utf-8') as fd:
        don = csv.writer(fd, delimiter=";")
        don.writerow(
            ["Nom equipe", "nombre des joueurs ", "nombre d'equestion  vrai", "nombre d'equestion  fausse","Nombre des bombes", "total", "win/loss", "Classement"])
        don.writerow([score_groups[1]])
        don.writerow([score_groups[2]])
        don.writerow([score_groups[3]])
        don.writerow([score_groups[4]])
    
Liste_nombre_joures=[1,2,3,4,5,6,7,8,9]

def groupes(num_grp):
    grp = str(input(f"Nom du Groupe {num_grp}: "))
    nb1=int()
    while nb1 not in Liste_nombre_joures:
        try:
            nb1 = int(input("Nombres des joueurs : "))
        except ValueError:
            print("Erreur,veuillez saisir la valeur correct.")     
    print(f"Le groupe {num_grp} a été créé avec succès.")
    score_groups[num_grp]["Nom_grp"]=grp
    score_groups[num_grp]["membres"]=nb1

List_R=["Atlantique","Indien","Arctique","Pacifique","Italie","Espagne","France","Allemagne","H2O","CO2","O2","H2SO4","7","8","9","10","Isaac Newton","Albert Einstein","Charles Darwin","Galilee","Brésil","Argentine","Guépard","Faucon pèlerin","Lion","Antilope","2005","2007","2009","2010"
,"Swift","JavaScript","Java","C","C++","Python","Digital Network System","Domain Network Service","Domain Name System","Data Network Service","AMD","Intel","IBM","Texas Instruments","count()","length()","len()","size()","Supprime tous les éléments de la liste","Supprime le dernier élément de la liste","Supprime un élément spécifique de la liste","Ajoute un élément en fin de liste"
,"Ellen Johnson Sirleaf (Liberia)","Winnie Mandela (Afrique du Sud)","Joyce Banda (Malawi)","Ameenah Gurib-Fakim (Maurice)","9","8","7","6","9","19","29","39","8 m/s**2","5 m/s**2","15 m/s**2","20 m/s**2","De la matière","De la lumière","De l'énergie","De la chaleur","x<5","x>5","x>15","x<15","1965","1967","1969","1971"]

#-------------les questions --------------#
def rounds(nb_grp,l_qst,l_reponse):
    print(f"--------------le groupe {nb_grp}--------------")
    while True:
        try:
            NB= int(input("Veuillez choisir un nombre entre 1 et 24 : "))
            if NB in nombres_choisis:
                nombres_choisis.remove(NB)
                break
            else:
                pass
        except ValueError:
            print("Erreur !! veuillez entrer un nombre entier.")
    #choix par hasard du question
    question=(random.choice(l_qst))
    # indice de la ligne de hasard
    ligne_de_qst=l_qst.index(question)
    #affichage du qst
    for option in question:
        print("     ",option,"\n")
    #verification de la bomb
    if question[0]=="BOOM" :
        reponse_correct=l_reponse[ligne_de_qst]
        print("wow!! vous avez tout perdu  ")
        score_groups[nb_grp]["bomb"]+=1
        score_groups[nb_grp]["score"] =0
        l_qst.remove(question)
        l_reponse.remove(reponse_correct)
        pass
    else:
        reponse_utilisateur=str("")
        while reponse_utilisateur not in List_R:
            try:
                #reponse d'utilisateur
                reponse_utilisateur=input("votre reponse :")
                if reponse_utilisateur not in List_R:
                    raise ValueError("S'il vous plait, répétez encore.")
            except ValueError as e:
                print(f"Erreur,{e}")    
        #verification des reponse
        reponse_correct=l_reponse[ligne_de_qst]
        if reponse_utilisateur.lower().strip() == reponse_correct[0].lower():
            print(f"\n reponse est correct ! Vous avez gagné 100 pts")
            score_groups[nb_grp]["correct"] += 1
            score_groups[nb_grp]["score"] += 100
        else:
            print(f"\n Réponse incorrecte ! La bonne réponse était : {reponse_correct[0]}")
            score_groups[nb_grp]["incorrect"] += 1
        l_qst.remove(question)
        l_reponse.remove(reponse_correct)

#------------------------------debut de programme main-------------------------------------------------------#

print("--------------------------------Bienvenu Tous le monde--------------------------------")
print("   Introduction:")
print(
    "  -Le but du jeu est de répondre correctement aux questions. Les joueurs doivent travailler ensemble ou les uns \n"
    "contre les autres, selon le mode choisi, pour éviter une bombe ou une explosion.")
print(
    "  -Dans ce jeu, la class sera divisée en quatre groupes, chaque groupe étant composé d'au moins 4 à 5 personnes,\n"
    "et chaque groupe présentera un document composé du nom du groupe et des noms des membres du groupe, et il sera présenté à les organisateurs. Merci.")
print("\n")

#ouverture du fichier des question en lecture
with open("QST.csv", "r", encoding="utf-8") as fLQ:
    l_qst=list( csv.reader(fLQ, delimiter=";"))


#ouverture du fichier des reponse en lecture
with open("reponse.csv", "r", encoding="utf-8") as fLR:
    l_reponse=list( csv.reader(fLR, delimiter=";"))

# #creation des groupes
for nom_grp in range(1,5) :
    groupes(nom_grp)

while True:
    x=input("Taper star pour debuter le jeux ou stop pour arreter : ")
    if x.lower().strip() == "star" :
        menu()
        break
    if x.lower().strip() == "stop":
        print("programme quitter")
        quit()
    else:
        print(" Erreur !! veuillez repeter votre choix")

qst_rpns()    
# debut des qsts pour chaque groupes
for i in range(1,7):
    for NOMBRE_DU_GROUPE in range(1,5):
        rounds(NOMBRE_DU_GROUPE,l_qst, l_reponse)

open_lire_ficher()
