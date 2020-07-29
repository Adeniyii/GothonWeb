from nose.tools import *
from gothonweb.planisphere import *

def test_room():
    gold = Room('GoldRoom', 'This has some gold.')
    assert_equal(gold.name, 'GoldRoom')
    assert_equal(gold.description, 'This has some gold.')
    assert_equal(gold.paths, {})

def test_paths():
    center = Room('center', 'A room in the center.')
    earth = Room('earth', 'A room in the upper center.')
    hell = Room('hell', 'A room in the downward center.')
    center.add_paths({'up': earth, 'down': hell})

    assert_equal(center.go('up'), earth)
    assert_equal(center.go('down'), hell)

def test_map():
    center = Room('center', 'A room in the center.')
    earth = Room('earth', 'A room in the upper center.')
    hell = Room('hell', 'A room in the downward center.')
    corona = Room('corona', 'A room in the corona center.')
    abule = Room('abule', 'A room in abule iroko.')

    center.add_paths({'up': earth, 'down': hell, 'left': corona, 'right': abule})
    earth.add_paths({'down': center})
    hell.add_paths({'up': center})
    corona.add_paths({'right': center, 'up': earth, 'down': hell})
    abule.add_paths({'left': center, 'up': earth, 'down': hell})

    assert_equal(center.go('up').go('down'), center)
    assert_equal(earth.go('down').go('left'), corona)
    assert_equal(hell.go('up').go('right'), abule)

def test_gothon_game_map():
    start_room = load_room(START)
    assert_equal(start_room.go('shoot!'), death)
    assert_equal(start_room.go('dodge!'), death)

    broom = start_room.go('tell a joke')
    assert_equal(broom, laser_weapon_armory)

    next_room = broom.go('0132')
    assert_equal(next_room, the_bridge)
    assert_equal(broom.go('*'), death)
    assert_equal(next_room.go('throw the bomb'), death)
    assert_equal(next_room.go('slowly place the bomb'), escape_pod)

    last_room = (next_room.go('slowly place the bomb'))
    assert_equal(last_room.go('2'), the_end_winner)
    assert_equal(last_room.go('*'), the_end_loser)

    groom = name_room(escape_pod)
    assert_equal(groom, 'escape_pod')
    assert_equal(name_room(central_corridor), 'central_corridor')
    assert_equal(name_room(laser_weapon_armory), 'laser_weapon_armory')
    assert_equal(name_room(the_bridge), 'the_bridge')
    assert_equal(name_room(the_end_loser), 'the_end_loser')
    assert_equal(name_room(the_end_winner), 'the_end_winner')
    assert_equal(name_room(death), 'death')
    assert_equal(name_room(quips), 'quips')
    assert_equal(name_room(START), 'START')
