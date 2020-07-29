import random

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction)

    def add_paths(self, path):
        self.paths.update(path)


central_corridor = Room('Central Corridor',
"""
The Gothons of planet percal #25 have invaded your ship and destroyed your entire
crew. You are the last surviving member, and your last mission is to get the
neutron destruct bomb from the weapons armory, put it into the bridge and blow
the ship up after getting into an escape pod. You're running down the central
corridor to the weapons armory when a gothon jumps out, red scaly skin, dark
grimy teeth and evil clown cosyume flowing around his hate filled body.
He's blocking the way to the weapons armory and about to pull a gun to blast you.
""")

laser_weapon_armory = Room('Laser Weapon Armory',
"""
Luccky for you, they made you learn gothon insults in the academy. You tell the
gothon one joke you know: vlak krusnukh thrakh mech, invhuk jath lipton juice.
The gothon stops, tries not to laugh, then bursts out laughing and can't move.
While he's laughing, lil uzi very runs up on him and sprays him in the medulla
oblangata. You then burst through the weapon armory door.

You do a dive roll into the armory , crouch and scan the room for more gothons
in hiding. It's dead quiet, too quiet. You stand up and run to the far side of
the room and find the neutron bomb in it's container. There's a keypad lock on
the box and you need a code to get the bomb out. If you get the code wrong 10
times, the lock closes forever and you can't get the bomb. The code is 3 digits.
""")

the_bridge = Room('The Bridge',
"""
The container click, and the seal breaks letting gas out. You grab the bomb and
run as fast as you can to the bridge where you must place it in the right spot.
You burst onto the bridge with the neutron destruct bomb under your arm and
surprise 5 gothons who are trying to take control of the ship. Eack of them has
an even uglier clown costume than the last. They haven't pulled their weapons
out yet, as they see the bomb under your arm and don't want to set it off.
""")

escape_pod = Room('Escape Pod',
"""
You point your blaster at the bomb under your arm and the gothons put their hands
up and begin to sweat. You inch backward towards the door, open it, and slowly
place the bomb down while pointing your blaster at it. You then jump back through
the door, punch close button and blast the lock so the gothons can't get out.
Now that the bomb is placed, you run to the excape pod to get off this tin can.
You rush through the space ship, desperately trying to make it the the escape Pod
before the whole ship explodes. It seems like hardly any gothons are on the ship,
so your run is clear of interference. You get to the chamber with the escape pods
and now have to choose one to take. Some of the could be damaged but you don't
have time to look. There's 5 pods, which one do you take?
""")

the_end_winner = Room('The End',
"""
You jump into pod 2 and hit the eject button. The pod easily slides into space
and heads to the planet below. As it flies, you look back to see your ship implode
and then explode like a bright star, taking out the gothon ship at the same time.
You won.
""")

the_end_loser = Room('The End',
"""
You jump into a random pod and hit the eject button. The pod slides out into the
void of space, then implodes as the hull ruptures, crushing your body into peanut
butter.
""")


quips = [
"I have a small dog that's better at this.",
"Your president would be proud.",
"You suck at this.",
"Pipe", 
"Deji could do better than this."
]

death = Room('death', f'You died. {random.choice(quips)}')

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

the_bridge.add_paths({
    'throw the bomb': death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': death
})

central_corridor.add_paths({
    'shoot!': death,
    'dodge!': death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor' # -- key


def load_room(name):
    return globals().get(name)

def name_room(room):
    for key, value in globals().items():
        if value == room:
            return key
