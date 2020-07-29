from nose.tools import *
from parsers import lexicon


def test_directions():
    assert_equal(lexicon.scan('up', lexicon.pairs), [('direction', 'up')])

    result = lexicon.scan('away over down', lexicon.pairs)

    assert_equal(result, [('direction', 'away'),
                        ('direction', 'over'),
                        ('direction', 'down')])


def test_verbs():
    assert_equal(lexicon.scan('go', lexicon.pairs), [('verb', 'go')])
    result = lexicon.scan('go kill eat', lexicon.pairs)
    assert_equal(result, [('verb', 'go'),
                        ('verb', 'kill'),
                        ('verb', 'eat')])


def test_stops():
    assert_equal(lexicon.scan('the', lexicon.pairs), [('stop', 'the')])
    result = lexicon.scan('the in of', lexicon.pairs)
    assert_equal(result, [('stop', 'the'),
                        ('stop', 'in'),
                        ('stop', 'of')])


def test_nouns():
    assert_equal(lexicon.scan('gothons', lexicon.pairs), [('noun', 'gothons')])
    result = lexicon.scan('gothon fuckers', lexicon.pairs)
    assert_equal(result, [('noun', 'gothon'),
                        ('noun', 'fuckers')])


def test_numbers():
    assert_equal(lexicon.scan('1234', lexicon.pairs), [('number', '1234')])
    result = lexicon.scan('3 91234', lexicon.pairs)
    assert_equal(result, [('number', '3'),
                        ('number', '91234')])


def test_errors():
    assert_equal(lexicon.scan('ASDFGHJKL', lexicon.pairs), [('error', 'ASDFGHJKL')])
    result = lexicon.scan('bear ias princess.', lexicon.pairs)
    assert_equal(result, [('error', 'bear'),
                        ('error', 'ias'),
                        ('error', 'princess')])


def test_combo():
    result = lexicon.scan('north. 4, b.ear, 2. go in cag.e 500 PRincess,', lexicon.pairs)
    assert_equal(result, [('error', 'north'),
                        ('number', '4'),
                        ('error', 'b.ear'),
                        ('number', '2'),
                        ('verb', 'go'),
                        ('stop', 'in'),
                        ('error', 'cag.e'),
                        ('number', '500'),
                        ('error', 'PRincess')])
