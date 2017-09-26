#from peewee import *
import acquire_data as data
from playhouse.migrate import *


db = SqliteDatabase('shot_charts.db')

class Shot(Model):
    gameId = CharField() #make foreign key field for games table?
    gameEventId = CharField() ## make foreign key field?
    playerId = CharField()
    playerName = CharField()
    teamId = CharField()
    teamName = CharField()
    period = IntegerField()
    minutesRem = IntegerField()
    secondsRem = IntegerField()
    eventResult = CharField() #event type
    actionType = CharField()
    shotType = CharField()
    shotZoneBasic = CharField()
    shotZoneArea = CharField()
    shotZoneRange = CharField()
    shotDistance = CharField()
    locX = IntegerField()
    locY = IntegerField()
    shotMadeFlag = BooleanField()
    gameDate = DateField()
    homeTeam = CharField()
    awayTeam = CharField()

    class Meta:
        database = db

def initialize():
    """create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Shot], safe = True)

def get_shot_chart_dictionary(game, headers):
    shotChart = {}
    for i in range(len(headers)):
        header = headers[i]
        value = game[i]

        shotChart[header] = value
    return shotChart

def add_shots(shotsData, headers):
    for i in range(len(shotsData)):
        game = shotsData[i]
        shotChart = get_shot_chart_dictionary(game, headers)
        add_shots_ind_game(shotChart)

def add_shots_ind_game(shotChart):
    try:
        shotMade = True
        if shotChart['SHOT_MADE_FLAG'] == 0:
            shotMade = False
        Shot.create(gameId=shotChart['GAME_ID'], gameEventId=shotChart['GAME_EVENT_ID'], playerId=shotChart['PLAYER_ID'],
                    playerName=shotChart['PLAYER_NAME'], teamId=shotChart['TEAM_ID'], teamName=shotChart['TEAM_NAME'],
                    period=shotChart["PERIOD"], minutesRem=shotChart['MINUTES_REMAINING'], secondsRem=shotChart['SECONDS_REMAINING'],
                    eventResult=shotChart['EVENT_TYPE'], actionType=shotChart['ACTION_TYPE'], shotType=shotChart['SHOT_TYPE'],
                    shotZoneBasic=shotChart['SHOT_ZONE_BASIC'], shotZoneArea=shotChart['SHOT_ZONE_AREA'],
                    shotZoneRange=shotChart['SHOT_ZONE_RANGE'], shotDistance=shotChart['SHOT_DISTANCE'],
                    locX=shotChart['LOC_X'], locY=shotChart['LOC_Y'], shotMadeFlag=shotMade, gameDate=shotChart['GAME_DATE'],
                    homeTeam=shotChart['HTM'], awayTeam=shotChart['VTM'])
    except IntegrityError:
        print shotChart

def write_shots_to_database():
    inDatabase = []
    for player in Shot.select(Shot.playerId).distinct():
        inDatabase.append(player.playerId)
    playerIds = data.upload_from_json("player_ids")
    for id in playerIds:
        if id not in inDatabase:
            playerData = data.upload_from_json("shot_charts/{}".format(id))
            shot_headers = playerData['headers']
            shots = playerData['rowSet']
            add_shots(shots, shot_headers)

def get_player_shots_db(playerId):
    playerShots = []
    for shotChart in Shot.select().where(Shot.playerId == playerId):
        playerShots.append(shotChart)
    return playerShots

def get_player_shots_clutch_db(playerId):
    playerShots = []
    for shotChart in Shot.select().where(Shot.playerId == playerId, Shot.period == 4, Shot.minutesRem <= 5):
        playerShots.append(shotChart)
    return playerShots

def get_team_images(team_id):
    images = {}
    for shotChart in Shot.select().where(Shot.teamId == team_id):
        link = "{}.png".format(shotChart.playerId)
        if link not in images:
            images[link] = shotChart.playerId
    return images

def get_team_names():
    names = {}
    for name in Shot.select(Shot.teamName, Shot.teamId).distinct():
        names[name.teamId] = name.teamName
    return names

def get_players_for_team(team_id):
    player_ids = []
    for record in Shot.select(Shot.playerId).where(Shot.teamId == team_id).distinct():
        player_ids.append(record.playerId)
    return player_ids


# initialize()
# write_shots_to_database()


