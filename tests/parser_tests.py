from nose.tools import *
from parsers import lexicon
from parsers.parser import *


wordlist = lexicon.scan('now go and bear run north and the south', lexicon.pairs)
wordlist2 = lexicon.scan('the run bear south', lexicon.pairs)
wordlist3 = lexicon.scan('run north, and eat the princess', lexicon.pairs)
wordlist4 = lexicon.scan('down north', lexicon.pairs)
wordlist5 = lexicon.scan('barthelonya barthelomeu, shuperu', lexicon.pairs)
extra = lexicon.scan('now bear go to the north princess. ', lexicon.pairs)


def test_peek():
    result = peek(wordlist)
    result2 = peek(wordlist2)
    result3 = peek(wordlist3)
    result4 = peek(wordlist4)
    result5 = peek(wordlist5)

    assert_equal(result, 'stop')
    assert_equal(result2, 'stop')
    assert_equal(result3, 'verb')
    assert_equal(result4, 'direction')
    assert_equal(result5, 'error')


def test_parse_verb():
    native_result = parse_verb([('stop', 'now'), ('verb', 'run'),('direction', 'down')])
    result = parse_verb(wordlist)
    assert_equal(result, ('verb', 'go'))
    assert_equal(native_result, ('verb', 'run'))


def test_parse_subject():
    native_result = parse_subject([('stop', 'and'), ('verb', 'run'), ('direction', 'north')])
    assert_equal(native_result, ('noun', 'player'))


def test_parse_object():
    native_result = parse_object([('noun', 'bear'), ('direction', 'down')])
    assert_equal(native_result, ('noun', 'bear'))


def test_parse_sentence():
    native_result = parse_sentence([('stop', 'now'), ('verb', 'fuck'), ('stop', 'the'),
                    ('noun', 'princess'), ('stop', 'the'), ('noun', 'princess')])

    assert_equal(native_result, 'fuck princess')


def test_exceptions():

    assert_raises(ParserError, parse_subject, wordlist4)
    assert_raises(ParserError, parse_verb, wordlist5)
    assert_raises(ParserError, parse_object, wordlist5)
