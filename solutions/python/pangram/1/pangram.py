def is_pangram(sentence):
    sentence = sentence.lower()
    sentence_list = sentence.replace('.','').strip().replace(' ','')
    letter_list = [i for i in sentence_list if i.isalpha()]
    letter_set = set(letter_list)


    if len(letter_set) == 26:
        return True
    return False
