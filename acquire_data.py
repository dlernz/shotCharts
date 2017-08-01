import requests
import csv,json

user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 '
                            'Safari/537.36'}


def upload_from_json(filename):
    with open('shot_charts/{}.json'.format(filename), 'r') as fp:
        data = json.load(fp)
        return data

def save_json(filename, data):
    with open('shot_charts/{}.json'.format(filename), 'w') as fp:
        json.dump(data, fp)

def get_player_ids(user_agent):
    players_url = "http://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&" \
                  "Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&" \
                  "GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base" \
                  "&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame" \
                  "&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=" \
                  "2016-17&SeasonSegment=&SeasonType=Playoffs&ShotClockRange=&StarterBench=&" \
                  "TeamID=0&VsConference=&VsDivision=&Weight="

    response = requests.get(players_url, headers = user_agent)
    response.raise_for_status()
    data = response.json()['resultSets'][0]
    player_stats = data['rowSet']
    player_ids = {}

    for player in player_stats:
        player_id = player[0]
        player_ids[player_id] = player[1]
    save_json("player_ids", player_ids)

def get_player_shots(player_id, user_agent):
    shots_url = "http://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=33&" \
                "CFPARAMS=2016-17&ClutchTime=&Conference=&ContextFilter=&ContextMeasure" \
                "=FGA&DateFrom=&DateTo=&Division=&EndPeriod=10&EndRange=28800&GROUP_ID=" \
                "&GameEventID=&GameID=&GameSegment=&GroupID=&GroupMode=&GroupQuantity=5&" \
                "LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&OpponentTeamID=0&Outcome=" \
                "&PORound=0&Period=0&PlayerID={0}&PlayerID1=&PlayerID2=&PlayerID3=&" \
                "PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&RangeType=0&" \
                "RookieYear=&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&S" \
                "hotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=0&VsConf" \
                "erence=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=" \
                "&VsPlayerID5=&VsTeamID=".format(player_id)

    response = requests.get(shots_url, headers = user_agent)
    response.raise_for_status()
    data = response.json()['resultSets'][0]
    save_json(player_id, data)


def get_shot_charts(player_ids):
    for player_id in player_ids:
        get_player_shots(player_id, user_agent)

def write_shots_to_csv(filename, shot_headers, shot_charts):
    shot_charts.append(shot_headers)
    with open(filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(shot_charts)

def get_target_shot(player_id, shot_id):
    target_shot = []
    headers = []
    with open('shot_charts/{}.json'.format(player_id), 'r') as fp:
        data = json.load(fp)
        print data.keys()
        shots = data['rowSet']
        headers = data['headers']
        for item in shots:
            print item[2]
            if item[2] == shot_id:
                target_shot = item

    shotChart = {}
    for i in range(len(headers)):
        header = headers[i]
        value = target_shot[i]
        shotChart[header] = value

    with open('testing/{}.json'.format(shot_id), 'w') as fp:
        json.dump(shotChart, fp)
    return shotChart

def get_file_json(filename):
    with open('{}.json'.format(filename), 'r') as fp:
        data = json.load(fp)
        return data

def save_player_images():
    player_ids = get_file_json("player_ids")
    for player in player_ids:
        url = "http://stats.nba.com/media/players/230x185/{}.png".format(player)
        response = requests.get(url)
        if response.status_code == 200:
            with open("static/images/{}.png".format(player), 'wb') as f:
                f.write(response.content)
