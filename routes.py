from flask import Flask, render_template
import shots, json, acquire_data
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route('/court')
def court():
    playerShots = shots.get_player_shots_db("202322")
    playerDicts = []
    for item in playerShots:
        json_data = json.dumps(model_to_dict(item))
        playerDicts.append(json_data)
    return render_template('court.html', playerShots = playerDicts)  # render a template

@app.route('/')
def hello_world():
    playerShots = ""
    return render_template('index.html', playerShots = playerShots)

@app.route('/team/<team_id>')
@app.route('/team')
def team(team_id="1610612764", player_id="1627849"):
    return load_team_page_data(team_id, player_id)

@app.route('/team/<team_id>/<player_id>')
def team_loaded(team_id, player_id):
    return load_team_page_data(team_id, player_id, False)

# TODO: Clean up templates so images don't have to be pulled every load, just refresh shot page (make modules of page)
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


@app.route('/test')
def testing():
    #target_shot = acquire_data.get_target_shot(202322, 271)
    #output = [target_shot]
    return render_template('test.html', output = "hello")

@app.route('/hello')
def hello():
    data = {'username': 'Pang', 'site': 'stackoverflow.com'}
    return render_template('settings_trash.html', data=data)

if __name__ == '__main__':
    app.run()