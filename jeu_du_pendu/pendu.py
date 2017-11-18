import pickle
from jeu_du_pendu.donnees import list_total_words
from jeu_du_pendu.fonction import *

is_in_life = True
while is_in_life == True:
    for current_word in list_total_words:
        if is_in_life == False:
            break
        is_not_finish = True
        nb_try = len(current_word)
        while is_not_finish:
            display_word = show_word(current_word)
            print(display_word)

            print("nombre de coup : " + str(nb_try))
            answer = input("Veuillez saisir une reponse : ")
            result = play_a_answer(current_word, answer)

            if result:
                word = "".join([l[0] for l in current_word])
                last_word = "".join([l[0] for l in list_total_words[len(list_total_words)-1]])
                if word == last_word and check_if_win(current_word):
                    print("Bravo ! le mot à trouver etait : " +  word)
                    print("\n\nFelicitation vous avez gagné !!")
                    is_in_life = False
                    is_not_finish = False
                    break

                if check_if_win(current_word):
                    print("Bravo ! le mot à trouver etait : " + word)
                    is_not_finish = False
                    break
            else:
                nb_try -= 1
                if nb_try == 0:
                    is_in_life = False
                    is_not_finish = False
                    break
                else:
                    display_word = show_word(current_word)
                    print(display_word + "\n")

print("La partie est terminé !!")
