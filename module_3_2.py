def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word in word:
            same_words.append(word)
    print(f'среди слов {other_words} слова с корнем «{root_word}» следующие:\n{same_words}')


def single_root_words2(root_word, *other_words):
    same_words2 = [word for word in other_words if word.lower() in root_word.lower()]
    print(f'В главном слове «{root_word}» из слов {other_words} встречаются (без учета регистра) следующие:\n{same_words2}')


single_root_words('тук', 'катук', 'тукан', 'ступка', 'спам', 'утка', 'тик', 'истукан')

single_root_words2('Labamba', 'bomba', 'labmda', 'Bam', 'Abama', 'Ambal', 'balda', 'lab')
