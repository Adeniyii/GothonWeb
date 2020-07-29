from nose.tools import *
from app import app


app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)

def test_game():
    rv = web.get('/game', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Central Corridor", rv.data)

    data = {'action': 'tell a joke', 'name': 'action'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_in(b"Laser Weapon Armory", rv.data)

    data = {'action': '0132', 'name': 'action'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_in(b"The Bridge", rv.data)

    data = {'action': 'slowly place the bomb', 'name': 'action'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_in(b'Escape Pod', rv.data)

    data = {'action': '2', 'name': 'action'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_in(b'The End', rv.data)


def test_session():
    with web.session_transaction() as sess:
        sess['abule_iroko'] = 'trouble_man'

    web.get('/')
    assert_equal(sess['abule_iroko'], 'trouble_man')
