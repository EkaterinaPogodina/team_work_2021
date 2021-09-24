def only_str(funct):
    def new_funct(data):
        new_data = []
        for el in data:
            if type(el) == type('a'):
                new_data.append(el)
        funct(new_data)

    return new_funct


@only_str
def consonants(data):
    alph = 'qwrtpsdfghjklzxcvbnm'
    for word in data:
        for letter in word:
            if letter.lower() in alph:
                print(letter, end='')
    print()


@only_str
def lenth5(data):
    for word in data:
        if len(word) > 5:
            print(word)


'''
Тесты:
consonants([23, 'ffdasasd', 'ds', True])
lenth5([23, 'ffdasasd', 'ds', True])
'''
