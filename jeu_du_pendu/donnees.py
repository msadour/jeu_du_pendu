list_words = [
    "sql",
    "git",
    "css",
    "html",
    "linux",
    "python",
    "windows",
]

"""
list_total_words will loke like it : [ [["A', False], ['B', False]], [["A', False], ['B', False]] ...]
where False mean that the letter is not display
"""

list_total_words = []
for a_word in list_words:
    list_of_a_word = [[a_letter, False] for a_letter in a_word]
    list_total_words.append(list_of_a_word)
