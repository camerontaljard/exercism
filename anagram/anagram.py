import string

word_dic = dict()
anagram_dic = dict()
match_lst = list()


def detect_anagrams(word, anagram):

    print word

    for letter in word.lower():
        if letter not in word_dic:
            word_dic[letter] = 1
        else:
            word_dic[letter] += 1

    for x in range(0, len(anagram)):
        _anagram = anagram[x]

        for letter in _anagram.lower():
            if letter not in anagram_dic:
                anagram_dic[letter] = 1
            else:
                anagram_dic[letter] += 1

        if word_dic == anagram_dic:
            #print word, 'equals', _anagram
            match_lst.append(_anagram)

        anagram_dic.clear()
    return match_lst
    match_lst[:] = []
    #word_dic.clear()



detect_anagrams('master', 'stream pigeon maters'.split())
detect_anagrams('listen', 'enlists google inlets banana'.split())
detect_anagrams('orchestra', 'cashregister Carthorse radishes'.split())
detect_anagrams('allergy', 'gallery ballerina regally clergy largely leading'.split())
detect_anagrams('banana', ['banana'])
