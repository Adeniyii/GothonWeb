from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)
@app.route('/')

def index():
    #  this is used to "setup" the session with starting values; planisphere.START represents a room object "key"
    session['room_name'] = planisphere.START
    return redirect(url_for("gamed"))


@app.route('/games', methods=['GET', 'POST'])
def gamed():
    #  room_name stores the first room in the map that was stored in START--central_corridor
    room_name = session.get('room_name')
    #  this block is meant to request and reload the Pages using the GET method.. Pages are usually requested using GET.
    if request.method == "GET":
        #  if a room object "value" has been stored in the current session and stored in the room_name variable. check the def_index() function
        if room_name:
            #  this copies the room object into the room variable.
            room = planisphere.load_room(room_name)
            #  call the "show_room" html file and pass the room object to the file. note that room is a class object and hass been assigned attributes in planisphere.
            return render_template("show_room.html", room=room)
        #  if room_name was assigned no room object, return the "you_died" html page.
        else:
            #  why is there here? do you need it?
            return render_template("you_died.html")

    #  if request method is POST.. This changes to post once the show_room html form is called, as the form was assigned the POST method.
    #  this block basically handles the form, collects info from the form and uses the info to modify the web page.
    else:
        # action is the answer the user submits to the form
        action = request.form.get('action')
        #  if room_name and action are currently given, i.e if the user has submitted an answer to the form
        if room_name and action:
            #  this copies the room object into the room variable.
            room = planisphere.load_room(room_name)
            #  collects the object of the next room using the inputted answer(action) from the form.
            next_room = room.go(action)
            #  if no answer was provided in the form
            if not next_room:
                #  map the room_name session key to the current room's key.
                session['room_name'] = planisphere.name_room(room)
            #  if an answer was provided in the form.
            else:
                #  modify the room_name session key to the next room's key.
                session['room_name'] = planisphere.name_room(next_room)
        #  reload the page with the newly edited session key for the next room. This resets the request method to GET and runs the first if block.
        return redirect(url_for('gamed'))


app.secret_key = 'johnnybb01'

if __name__== "__main__":
    app.run()
