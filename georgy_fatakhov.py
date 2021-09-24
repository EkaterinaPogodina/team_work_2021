def only_str(funct):  # only strings - тольк строки
    def new_funct(data):  # декоратор фильтрует все нестроки
        new_data = []
        for el in data:
            if type(el) == type('a'):
                new_data.append(el)
        funct(new_data)

    return new_funct


@only_str
def consonants(data):  # consonants это согласные,
    alph = 'qwrtpsdfghjklzxcvbnm'  # данная функция выводит их в строчку
    for word in data:
        for letter in word:
            if letter.lower() in alph:
                print(letter, end='')
    print()


@only_str
def lenth5(data):  # lenth5 в переводе с английского "длина 5",
    for word in data:  # функция выводит строкиидлиной больше 5
        if len(word) > 5:
            print(word)


'''
Тесты:
consonants([23, 'ffdasasd', 'ds', True])
lenth5([23, 'ffdasasd', 'ds', True])
'''
