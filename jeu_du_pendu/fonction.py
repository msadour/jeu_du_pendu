def check_if_letter_in_word(letter_answer, list_of_the_word):
    """
    check if letter is in word
    :param letter_answer:
    :param list_of_the_word:
    :return:
    """
    nb_found = 0
    for a_letter in list_of_the_word:
        if letter_answer == a_letter[0]:
            nb_found += 1
    if nb_found > 0:
        return True
    else:
        False

def play_a_answer(list_of_the_word, answer=""):
    """
    try to play a answer
    :param liste_du_mot:
    :param reponse:
    :return:
    """
    if len(answer) == 1:
        if check_if_letter_in_word(answer, list_of_the_word):
            for a_letter in list_of_the_word:
                if answer == a_letter[0]:
                    a_letter[1] = True
            return True
        else:
            return False
    else:
        liste_lettre_du_mot = [l[0] for l in list_of_the_word]
        word_str = "".join(liste_lettre_du_mot)
        if answer == word_str:
            for a_letter in list_of_the_word:
                a_letter[1] = True
            return True
        else:
            return False

def show_word(list_of_the_word):
    """
    show the word in the console
    :param list_of_the_word:
    :return:
    """
    word_for_show = ""
    for letter in list_of_the_word:
        letter = '*' if letter[1] == False else letter[0]
        word_for_show = word_for_show + letter
    return word_for_show

def check_if_win(list_of_the_word):
    """
    check if all the word is display
    :param liste_du_mot:
    :return:
    """
    liste_displayed_word = [word[1] for word in list_of_the_word]
    if False not in liste_displayed_word:
        return True
    else:
        return False