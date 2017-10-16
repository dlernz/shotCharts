from flask import Flask, render_template, request, jsonify
import shots, json, acquire_data
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

# TODO: remove shots outside of court area
# TODO: Assign some marker of active team and selected player -- internal and external
# TODO: Clutch shots filter -- only show shots shot in crunch time -- link to active team and selected player
# TODO: Modify court colors/banner border to match team colors
# TODO: Add index to columns in DB
# TODO: Clean up draw_court.js code;
# TODO: remove extra space in div for court

@app.route('/court')
def court():
    playerShots = shots.get_player_shots_db("202322")
    playerDicts = []
    for item in playerShots:
        json_data = json.dumps(model_to_dict(item))
        playerDicts.append(json_data)
    return render_template('court.html', playerShots = playerDicts)

@app.route('/team')
def team(team_id="1610612764", player_id="1627849"):
    req_team_id = request.args.get('team_id')
    req_player_id = request.args.get('player_id')
    if req_team_id is not None or req_player_id is not None:
        return load_team_page_data(req_team_id, req_player_id)
    return load_team_page_data(team_id, player_id)

@app.route('/changePlayer')
def team_loaded():
    player_id = request.args.get('player_id')
    team_id = request.args.get('team_id')
    return load_player_shots(team_id, player_id, new_load = False)

@app.route('/clutch' )
def clutch(team_id="1610612764", player_id="1627849"):
    return load_team_page_data(team_id, player_id, clutch = True, new_load = False)

def load_player_shots(team_id, player_id, clutch = False, new_load = False):
    playerShots = []
    output = []
    players = shots.get_players_for_team(team_id)
    if new_load:
        player_id = players[0]
    if clutch:
        playerShots = shots.get_player_shots_clutch_db(player_id)
    else:
        playerShots = shots.get_player_shots_db(player_id)

    for item in playerShots:
        output.append(model_to_dict(item))
    return jsonify(output)

def load_team_page_data(team_id, player_id, clutch = False, new_load = True):
    playerDicts = []
    playerShots = []
    names = shots.get_team_names()
    players = shots.get_players_for_team(team_id)
    if new_load:
        player_id = players[0]

    if clutch:
        playerShots = shots.get_player_shots_clutch_db(player_id)
    else:
        playerShots = shots.get_player_shots_db(player_id)

    for item in playerShots:
        json_data = json.dumps(model_to_dict(item))
        playerDicts.append(json_data)

    images = shots.get_team_images(team_id)
    return render_template('court.html', playerShots=playerDicts, team_images=images, names=names, team_id=team_id)

if __name__ == '__main__':
    app.run()