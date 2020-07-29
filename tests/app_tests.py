from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()


def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'CENTRAL CORRIDOR', rv.data)



def test_help():
    rv = web.get('/help', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'Game Manual For Super DUMMIES', rv.data)
    


def test_game():
    data = {'action': 'tell them a joke'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_equal(rv.status_code, 200)
    assert_in(b'LASER WEAPON ARMORY', rv.data)

    data = {'action': "000"}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_equal(rv.status_code, 200)
    assert_in(b'THE BRIDGE', rv.data)

    data1 = {'action': "attack the gothons"}
    vr = web.post('/game', follow_redirects=True, data=data1)
    assert_equal(vr.status_code, 200)
    assert_in(b'DEATH', vr.data)

    data = {'action': "use king's haki"}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_equal(rv.status_code, 200)
    assert_in(b'ESCAPE POD', rv.data)

    data = {'action': "2"}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_equal(rv.status_code, 200)
    assert_in(b'WINNER', rv.data)
