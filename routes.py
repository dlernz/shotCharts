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

@app.route('/team/<player_id>')
@app.route('/team')
def team(player_id = "202322"):
    playerDicts = []
    playerShots = shots.get_player_shots_db(player_id)
    one_shot = model_to_dict(playerShots[0])
    for item in playerShots:
        json_data = json.dumps(model_to_dict(item))
        playerDicts.append(json_data)

    team_id = one_shot['teamId']
    images = shots.get_team_images(team_id)
    return render_template('court.html', playerShots = playerDicts, team_images = images )

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