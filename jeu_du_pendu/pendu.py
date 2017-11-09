import pickle
from donnees import liste_total_mot
from fonction import *


global encore_en_vie
encore_en_vie = True
while encore_en_vie == True:
    for le_mot in liste_total_mot:
        if encore_en_vie == False:
            break
        est_pas_fini = True
        nb_coup = len(le_mot)
        while est_pas_fini:
            mot_visible = visualiser_mot(le_mot)
            print(mot_visible)

            print("nombre de coup : " + str(nb_coup))
            reponse = input("Veuillez saisir une reponse : ")
            resultat = jouer_une_lettre(le_mot, reponse)

            if resultat:
                mot_courant = "".join([l[0] for l in le_mot])
                dernier_mot = "".join([l[0] for l in liste_total_mot[len(liste_total_mot)-1]])
                if mot_courant == dernier_mot and verifie_si_gagner(le_mot):
                    print("Bravo ! le mot à trouver etait : " +  mot_courant)
                    print("\n\nFelicitation vous avez gagné !!")
                    encore_en_vie = False
                    est_pas_fini = False
                    break

                if verifie_si_gagner(le_mot):
                    print("Bravo ! le mot à trouver etait : " + mot_courant)
                    est_pas_fini = False
                    break
            else:
                nb_coup -= 1
                if nb_coup == 0:
                    encore_en_vie = False
                    est_pas_fini = False
                    break
                else:
                    mot_visible = visualiser_mot(le_mot)
                    print(mot_visible + "\n")

print("La partie est terminé !!")
