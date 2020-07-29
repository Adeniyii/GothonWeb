d = 'direction'
v = 'verb'
s = 'stop'
n = 'noun'
a = 'adjective'
p = 'pronoun'


pairs = {'right': d, 'left': d, 'down': d, 'up': d, 'away': d, 'over': d,
        'go': v, 'kill': v, 'run': v,'eat': v, 'shoot': v, 'dodge': v, 'tell': v, 'attack': v, 'blow': v, 'jump': v, 'place': v,
        'the': s, 'to': s, 'and': s, 'in': s, 'of': s, 'now': s, 'a': s,
        'gothon': n, 'bomb': n, 'gothons': n, 'joke': n, 'fuckers': n,
        'slowly': a, 'quickly': a,
        'them': p, 'their': p,
        }


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
