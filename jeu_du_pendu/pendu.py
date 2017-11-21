import pickle
from jeu_du_pendu.donnees import list_total_words
from jeu_du_pendu.fonction import *

your_nickname = input("Veuillez saisir votre pseudo/identifiant : ")
#We get the file's score for check if we must create new nickname or get the last score about a nickname puting
with open("scores.dat", "rb") as f:
    score_dict = pickle.load(f)
    if your_nickname not in score_dict.keys():
        score_dict = {your_nickname : 0}
        print("Bienvenue " + your_nickname + " ! Etant donnée que vous etes nouveau on vient de vous enregistrer dans "
                                             "notre fichier de score.")
    else:
        print("Bienvenue " + your_nickname + " ! votre score de la derniere fois etait : " + str(score_dict[your_nickname]) )

game_is_finish = True
nb_try = 4
while game_is_finish == True:
    for current_word in list_total_words:
        if game_is_finish == False:
            break
        word_is_not_finish = True
        while word_is_not_finish:
            display_word = show_word(current_word)
            print(display_word)
            print("nombre de coup restant : " + str(nb_try))
            answer = input("Veuillez saisir une reponse : ")
            result = play_a_answer(current_word, answer)

            if result:
                word = "".join([l[0] for l in current_word])
                last_word = "".join([l[0] for l in list_total_words[len(list_total_words)-1]])
                if word == last_word and check_if_win(current_word): #we check if all the word was founded
                    print("Bravo ! le mot à trouver etait : " +  word)
                    print("\n\nFelicitation vous avez fini le jeu !!")
                    score_dict[your_nickname] += 1
                    game_is_finish = False
                    word_is_not_finish = False
                    break

                if check_if_win(current_word):
                    print("Bravo ! le mot à trouver etait : " + word)
                    word_is_not_finish = False
                    break
            else:
                nb_try -= 1
                if nb_try == 0: #When the number of try is 0, the game is finish
                    score_dict[your_nickname] -= 1
                    game_is_finish = False
                    word_is_not_finish = False
                    break
                else:
                    display_word = show_word(current_word)
                    print(display_word + "\n")

#we save the new score in the file
with open("scores.dat", "wb") as f:
    pickle.dump(score_dict, f)
print("La partie est terminé !!")
