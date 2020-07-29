from nose.tools import *
from gothonweb.planisphere import *


def test_room():
    gold = Room('Gold Room', 'A room full of gold.', None, None, None, None)
    assert_equal(gold.name, 'Gold Room')
    assert_equal(gold.description, 'A room full of gold.')


def test_paths():
    center = Room('center', 'A room at the center of the map', None, None, None, None)
    up = Room('arena', 'A room for gladiators', None, None, None, None)
    down = Room('wakanda', 'A room for elites', None, None, None, None)

    center.add_paths({'go up': up, 'go down': down})
    assert_equal(center.go('go up'), up)
    assert_equal(center.go('go down'), down)


def test_load_room_object():
    silver = load_room_object(START)
    assert_equal(START, 'central_corridor')
    assert_equal(silver, central_corridor)


def test_get_room_name():
    silver = load_room_object(START)
    bronze = get_room_name(silver)
    assert_equal(START, 'central_corridor')
    assert_equal(silver, central_corridor)
    assert_equal(bronze, 'central_corridor')


def test_game_map():
    start = load_room_object(START)
    assert_equal(start.go('shoot gothon'), None)
    assert_equal(start.go('tell joke'), laser_weapon_armory)

    assert_equal(laser_weapon_armory.go('000'), the_bridge)
    assert_equal(laser_weapon_armory.go('567'), None)

    assert_equal(the_bridge.go('slowly place the bomb'), None)
    assert_equal(the_bridge.go('use haki'), escape_pod)

    assert_equal(escape_pod.go('2'), the_end_winner)
    assert_equal(escape_pod.go(''), None)

