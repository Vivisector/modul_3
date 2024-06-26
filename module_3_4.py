def sep():
    print('=================')
def single_root_word(root_word, *other_words):
    same_words=[word for word in other_words if root_word in word]
    # return same_words
    print(f'корень слова «{root_word}» встречается в словах\n' + '\n'.join(same_words))

sep()
single_root_word('rich', 'richiest', 'orichalcum', 'goodrich', 'cheers', 'richies')
sep()

def single_root_word2(root_word, *other_words):
    same_words=[word for word in other_words if word in root_word.lower()]
    # return same_words
    print(f'в слове «{root_word}» встречаются слова\n' + '\n'.join(same_words))

single_root_word2('Discount', 'disc', 'discipline', 'count', 'con', 'isc')
sep()