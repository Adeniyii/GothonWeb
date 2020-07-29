from flask import session, redirect, Flask, url_for, escape, render_template, request
from gothonweb import planisphere
from parsers import parser
from parsers.parser import ParserError

app = Flask(__name__)


@app.route('/')
def index():
    session['room_name'] = planisphere.START
    session['room_input'] = None
    session['room_count'] = 0
    session['empty_refreshes'] = 0
    return redirect(url_for("game"))



@app.route('/help')
def help():
    return render_template("help.html")



@app.route('/game', methods=['GET', 'POST'])
def game():

    room_name = session.get('room_name')
    room_input = session.get('room_input')
    room_count = session.get('room_count')
    refreshes = session.get('empty_refreshes')
    cheat = session.get('cheat')
    cheat = planisphere.load_room_object(cheat)
    current_room = planisphere.load_room_object(room_name)
#======================================================================================================================================================#
    print('>>>> displayed_room: ', room_name)
#======================================================================================================================================================#
    if request.method == 'GET':

        if room_name:
            if room_input:
                return render_template('show_room.html', room=current_room, entry=room_input, count=room_count, refresh=refreshes, cheat=cheat)
            else:
                return render_template('show_room.html', room=current_room, count=room_count, refresh=refreshes)
        else:
            return render_template('you_died.html')
    
    else:
        session['empty_refreshes'] += 1
        user_input = request.form.get('action')
        refreshes = session.get('empty_refreshes')
#======================================================================================================================================================#
        print('>>>> user_input: ', user_input)
        print('>>>> refreshes: ', refreshes)
#======================================================================================================================================================#
        if user_input:
            session['room_count'] += 1
            session['empty_refreshes'] = 0
            room_count = session.get('room_count')
#======================================================================================================================================================#
            print('>>>> room_count: ', room_count)
#======================================================================================================================================================#
            try:
                parsed_input = planisphere.parse_input(user_input)
                print('>>>> user_input b4 parse: ', user_input)
                session['room_input'] = parsed_input
#======================================================================================================================================================#
                print('>>>> parsed_input: ', parsed_input)
#======================================================================================================================================================#
                if parsed_input not in current_room.paths:
                    return render_template('show_room.html', room=current_room, entry=parsed_input, count=room_count, refresh=refreshes)
            
                else:
                    session['cheat'] = planisphere.get_room_name(current_room)
                    next_room = current_room.go(parsed_input)
#======================================================================================================================================================#
                    print('>>>> next_room: ', planisphere.get_room_name(next_room))
#======================================================================================================================================================#
                    if next_room:
                        session['room_count'] = 0
                        session['room_name'] = planisphere.get_room_name(next_room)

                    else:
                        session['room_name'] = planisphere.get_room_name(room_name)
            except ParserError as pap:
#======================================================================================================================================================#
                print('>>> parser error bro: ', pap)
#======================================================================================================================================================#
                if user_input in current_room.paths:
                    next_room = current_room.go(user_input)
                    session['room_count'] = 0
                    session['room_name'] = planisphere.get_room_name(next_room)
                else:
                    pass

        
        return redirect(url_for('game'))


app.secret_key = 'Ahucnubcub73487387'

if __name__ == "__main__":
    app.run()
