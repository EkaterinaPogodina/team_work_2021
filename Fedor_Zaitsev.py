def filtering(func):
    def function_wrapper(some_list):
        """ filtering non-strings """
        new_list = list(filter(lambda x: type(x) == str, some_list))
        return func(new_list)
    return function_wrapper


@filtering
def consonants_from(some_list):
    """ printing all the consonants' occurrences """
    cons = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q',
            'R', 'S', 'T', 'V', 'W', 'X', 'Z',
            'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
            'r', 's', 't', 'v', 'w', 'x', 'z'}

    words = set(some_list)
    letters = words.intersection(cons)
    for letter in letters:
        print(letter, end=' ')
    print('')


@filtering
def long_words_from(some_list):
    """ printing all the words with length equals 6 or more """
    for word in some_list:
        if len(word) > 5:
            print(word, end=' ')

    print('')
