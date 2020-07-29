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
        return self.paths.get(direction, None)

    
    def add_paths(self, path):
        self.paths.update(path)



central_corridor = Room('CENTRAL CORRIDOR', 

"""
The gothons of planet percal #25 have invaded your ship and
destroyed your entire crew. You are the last surviving member
and your mission is to get the neutron destruct bomb from the
weapons armory, put it in the bridge, and blow up the ship after
getting into an escape pod. 
""", 
"""
You're running down the central
corridor to the weapons armory when a gothon jumps out.
Red scaly skin, dark grimy teeth and evil clown costume flowing
around his hate filled body. He's blocking the way to the armory
about to pull a weapon to blast you.
""",
"""
Quick on the draw, you yank out your blaster and fire it at the
gothon. His clown costume is flowing around his body, which throws
off your aim. Your laser hits his costume but misses him entirely.
This completely ruins the brand new costume his mother just got him,
which causes him to fly into an insane rage and blast you
repeatedly in the face until you are very dead. Then he eats you.
""",
"""
Like a world class boxer you dodge,	weave, slip	and slide right
as the gothon's laser cracks a laser past your head. In the
middle of your artful dodge, your foot slips and you bang your
head on the metal wall and pass out. You wake up shortly after
only to die as the gothon stomps on your head and eats you.
""",
"""
You reach for your gun, but your palms have become sweaty from the
fear of being eaten by gothons. You try to grip your gun,
but it slips and clatters to the ground. The chief gothon smiles
at his henchmen as you get a heart attack and die. The end.
""")



laser_weapon_armory = Room('LASER WEAPON ARMORY',

"""
Lucky for you, they made you learn gothon insults in the academy. You tell the
gothon one joke you know: vlak krusnukh thrakh mech, invhuk jath lipton juice.
The gothon stops, tries not to laugh, then bursts out laughing and can't move.
While he's laughing, lil uzi vert runs up on him and sprays him in the medulla
oblangata. You then burst through the weapon armory door.
""", 
"""
You do a dive roll into the armory , crouch and scan the room for more gothons
in hiding. It's dead quiet, too quiet. You stand up and run to the far side of
the room and find the neutron bomb in it's container. There's a keypad lock on
the box and you need a code to get the bomb out. If you get the code wrong 5
times, the bomb auto detonates and blasts the entire ship to smitherines.
The code is 3 digits.
""",
None,
None,
 """
The lock buzzes one last time and then you hear a sickening melting sound 
as the mechanism is fused together preparing to explode. Just then, a small
group of gothons notice you and begin to charge through the armory door.
You begin to laugh as they gather you with drooling, bloody mouths.
By the time the gothons realize whats happening, the bomb opens up
and swallows the entire ship into a magnificent implosion. The end. 
""")

c1 = random.randint(0, 1)
c2 = random.randint(1, 2)
c3 = random.randint(2, 3)

bomb_code = str(f'{c1}{c2}{c3}')



the_bridge = Room('THE BRIDGE', 
"""
The container clicks, and the seal breaks letting gas out. You grab the bomb and
run as fast as you can to the bridge where you must place it in the right spot.
""", 
"""
You burst onto the bridge with the neutron destruct bomb under your arm and
surprise 5 gothons who are trying to take control of the ship. Eack of them has
an even uglier clown costume than the last. They haven't pulled their weapons
out yet, as they see the bomb under your arm and don't want to set it off.
""", 
"""
In a panic you throw the bomb at the group of Gothons, and make a leap for the	
door. Right	as you drop	it, a Gothon shoots you right in the back killing you. As
you	die	you	see	another	Gothon frantically try to 	disarm	the	bomb.	
You	die	knowing	they will probably blow	up	when it	goes off.
""", 
"""
You unleash your king's haki unconsciously and everybody gets knocked out except the
chief gothon who smiles at your impudence.
""",
"""
The gothons get tired of your threats and rush at you in a bid to contain the
explosion from their chief. You freeze at their reaction and try to arm the bomb.
But it's too late as you feel an arm go through your belly. You watch as a gothon
swipes your head off with a vicious slap and your vision blackens.
The End.

""")



escape_pod = Room('ESCAPE POD',
"""
You point your blaster at the bomb under your arm and the chief gothon puts his hands
up and begins to sweat.
""", 
"""
You inch backward towards the door, open it, and slowly
place the bomb down while pointing your blaster at it. You then jump back through
the door, punch close button and blast the lock so the gothons can't get out.
Now that the bomb is placed, you run to the excape pod to get off this tin can
You rush through the space ship, desperately trying to make it the the escape Pod
before the whole ship explodes. It seems like hardly any gothons are on the ship,
so your run is clear of interference. You get to the chamber with the escape pods
and now have to choose one to take. Some of them could be damaged but you don't
have time to look. There's 5 pods, which one do you take?
""", None, None, 
"""
You jump into the excape pod and press the ignition. The dashboard pops up as the
voltron engine hums to life. You hurriedly hit eject and the escape pod shoots out
into the space below waiting for your next command. You set your coordinates for 
earth and press transmorgify, you feel a sharp clang below your feet where the engine
is, and you immediately know you were better of exploding with the gothons on your home ship.
The End.
""")


pod = random.randint(1, 3)
poddy = str(pod)



the_end_winner = Room('WINNER', 
f"""
You jump into pod {pod} and hit the eject button. The pod easily slides into space
and heads to the planet below. As it flies, you look back to see your ship implode
and then explode like a bright star, taking out the gothon ship at the same time.
You won.
""", None, None, None, None)



central_corridor.add_paths({
    'tell joke': laser_weapon_armory
})

laser_weapon_armory.add_paths({
    '000': the_bridge
})

the_bridge.add_paths({
    'use haki': escape_pod,
    'place bomb': escape_pod
})

escape_pod.add_paths({
    poddy: the_end_winner
})

START = 'central_corridor'


def load_room_object(room):
    return globals().get(room)


def get_room_name(room):
    for key, value in globals().items():
        if value == room:
            return key


def parse_input(word):
        word_list = scan(word, lex_dict)
        parsed = parser.parse_sentence(word_list)
        return parsed
