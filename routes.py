from flask import Flask, render_template
import shots, json, acquire_data
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

# TODO: remove shots outside of court area
# TODO: Clutch shots filter -- only show shots shot in crunch time
# TODO: Clean up templates so images don't have to be pulled every load, just refresh shot page (make modules of page)
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
    return render_template('court.html', playerShots = playerDicts)  # render a template

@app.route('/team/<team_id>')
@app.route('/team')
def team(team_id="1610612764", player_id="1627849"):
    return load_team_page_data(team_id, player_id)

@app.route('/team/<team_id>/<player_id>')
def team_loaded(team_id, player_id):
    return load_team_page_data(team_id, player_id, False)

def load_team_page_data(team_id, player_id, new_load = True):
    playerDicts = []
    names = shots.get_team_names()
    players = shots.get_players_for_team(team_id)
    if new_load:
        player_id = players[0]
    playerShots = shots.get_player_shots_db(player_id)

    for item in playerShots:
        json_data = json.dumps(model_to_dict(item))
        playerDicts.append(json_data)

    images = shots.get_team_images(team_id)
    return render_template('court.html', playerShots=playerDicts, team_images=images, names=names, team_id=team_id)

if __name__ == '__main__':
    app.run()