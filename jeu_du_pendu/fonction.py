def check_lettre_mot(lettre_saisie, liste_du_mot):
    """
    Permet de verifier si la lettre jouer est contenue dans le mot
    :param lettre_saisie:
    :param liste_du_mot:
    :return:
    """
    nb_trouve = 0
    for une_lettre in liste_du_mot:
        if lettre_saisie == une_lettre[0]:
            nb_trouve += 1
    if nb_trouve > 0:
        return True
    else:
        False

def jouer_une_lettre(liste_du_mot, reponse=""):
    """
    Permet au joueur de jouer une lettre (ou directement un mot)
    :param liste_du_mot:
    :param reponse:
    :return:
    """
    if len(reponse) == 1:
        if check_lettre_mot(reponse, liste_du_mot):
            for une_lettre in liste_du_mot:
                if reponse == une_lettre[0]:
                    une_lettre[1] = True
            return True
        else:
            return False
    else:
        liste_lettre_du_mot = [l[0] for l in liste_du_mot]
        str_mot = "".join(liste_lettre_du_mot)
        if reponse == str_mot:
            for une_lettre in liste_du_mot:
                une_lettre[1] = True
            return True
        else:
            return False

def visualiser_mot(liste_du_mot):
    """
    Permet de visualiser le mot à la console
    :param liste_du_mot:
    :return:
    """
    mot_a_visualise = ""
    for lettre in liste_du_mot:
        lettre = '*' if lettre[1] == False else lettre[0]
        # lettre = lettre[0]
        mot_a_visualise = mot_a_visualise + lettre
    return mot_a_visualise

def verifie_si_gagner(liste_du_mot):
    """
    Verifie si le mot complet a été trouvé (si l'etat de chaque lettre est a True, donc affiché)
    :param liste_du_mot:
    :return:
    """
    liste_etat = [etat[1] for etat in liste_du_mot]
    if False not in liste_etat:
        return True
    else:
        return False