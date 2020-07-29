from parsers import parser
from parsers.lexicon import *
import random



lex_dict = {

'attack': v, 'blow': v, 'jump': v, 'place': v, 'give': v, 'blast': v, 'tell': v, 'throw': v,
'go': v, 'kill': v, 'run': v,'eat': v, 'shoot': v, 'dodge': v, 'crack': v, 'use': v,
'the': s, 'to': s, 'and': s, 'in': s, 'of': s, 'now': s, 'a': s, 'on': s,
'gothon': n, 'bomb': n, 'gothons': n, 'joke': n, 'fuckers': n, 'leg': n, 
'right': d, 'left': d, 'down': d, 'up': d, 'away': d, 'over': d,
'head': n, 'blast': n, 'haki': n, 'gun': n, 
'slowly': a, 'quickly': a, "king's": a,
'them': p, 'their': p,
}


p = '000'.strip(',').strip('.').strip('!').lower()
print('>>>> ',p)
print(p.isdigit())
print(p.isalpha())

class Room(object):

    def __init__(self, name, d1, d2, d3, d4, d5):
        self.paths = {}
        self.name = name
        self.description = d1
        self.description2 = d2
        self.description3 = d3
        self.description4 = d4
        self.description5 = d5
        self.quips = [
            "I have a small dog that's better at this.",
            "Your president would be proud.",
            "You suck at this.",
            "You Bloody Pipe"
        ]

    

    def go(self, direction):
        wor = scan(direction, lex_dict)
        parsed = parser.parse_sentence(wor)
        return self.paths.get(parsed, None)

    
    def add_paths(self, path):
        self.paths.update(path)


def word_type(word, lexicon):
    word_s = word.strip(',').strip('.').strip('!')
    word_l = word_s.lower()
    lex = lexicon.get(word_l)
    if word_l in lexicon:
        return (lex, word_s)
    elif word_l not in lexicon and word_l.isalpha():
        return ('error', word_s)
    elif word_s.isdigit():
        raise ValueError
    else:
        return ('error', word_s)


def scan(word, lexicon):
    sentence = []
    word_list = word.split()

    for words in word_list:
        try:
            t = word_type(words, lexicon)
            sentence.append(t)
        except ValueError:
            word_n = words.strip('.').strip(',').strip('!')
            sentence.append(('number', word_n))
    return sentence

print(scan('000', lex_dict))
