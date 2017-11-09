liste_mots = [
    "sql",
    "git",
    "css",
    "html",
    "linux",
    "python",
    "windows",
]

"""
liste_total_mot sera sous la forme [ [["A', False], ['B', False]], [["A', False], ['B', False]] ...]
où False signifiant que le mot n'est pas affiché
"""

liste_total_mot = []
for un_mot in liste_mots:
    liste_du_mot = []
    for une_lettre in un_mot:
        liste_du_mot.append([une_lettre, False])
    liste_total_mot.append(liste_du_mot)
