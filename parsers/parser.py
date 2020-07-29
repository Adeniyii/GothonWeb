#  creates a custom exception. -- parser error
class ParserError(Exception):
    pass


#  sentence class to collect the sorted tuples as subject verb and object attributes
#  and extract the words from the tuples.
class Sentence(object):


    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


    #  method to collect and return the extracted words into a string sentence.
    def collate(self):
        if self.subject == 'player':
            return f'{self.verb} {self.object}'
        elif self.subject == 'number':
            return f'{self.subject}'
        else:
            return f'{self.subject} {self.verb} {self.object}'

#  method to check and return the type of the next word.
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


#  method to match the collected wordlist to the expected word type
#  and remove the inspected tuple from the word list.
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


#  method to remove a specified word type from a gived word list.
def skip(word_list, word_type):
    if word_list and word_type:
        while peek(word_list) == word_type:
            match(word_list, word_type)


#  method to match and return a verb tuple from the wordlist.
def parse_verb(word_list):
    for word in word_list:
        skip(word_list, 'stop')
        skip(word_list, 'pronoun')
        skip(word_list, 'adjective')
        

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError('Expected a verb next.')


#  method to match and return an object tuple from the wordlist.
def parse_object(word_list):
    for word in word_list:
        skip(word_list, 'stop')
        skip(word_list, 'pronoun')
        skip(word_list, 'adjective')
        
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError('Expected a noun or direction next.')


#  method to match and return a subject tuple from the wordlist.
def parse_subject(word_list):
    for word in word_list:
        skip(word_list, 'stop')
        skip(word_list, 'pronoun')
        skip(word_list, 'adjective')
        
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    elif peek(word_list) == 'number':
        return match(word_list, 'number')
    else:
        raise ParserError('Expected a verb or noun next.')


#  method to collect the parsed tuples and return a final sentence string.
def parse_sentence(word_list):
    sub = parse_subject(word_list)
    if sub[0] == 'number':
        return f'{sub[1]}'
    else:
        verb = parse_verb(word_list)
        obj = parse_object(word_list)

        x = Sentence(sub, verb, obj)
        return x.collate()
