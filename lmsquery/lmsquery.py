import urllib2
import json
import datetime
from lmsquery import constants

class LMSQuery():
    def __init__(self, host=constants.LMS_HOST, port=constants.LMS_PORT, player_id=""):
        self.host = host
        self.port = port
        self.server_url = "http://%s:%s/jsonrpc.js" % (self.host, self.port)
        self.player_id = player_id

    # Generic query
    def query(self, player_id="", *args):
        params = json.dumps({'id':1, 'method':'slim.request', 'params':[player_id, list(args)]})
        req = urllib2.Request(self.server_url, params)
        response = urllib2.urlopen(req)
        response_txt = response.read()
        return json.loads(response_txt)['result']
    
    def rescan(self):
        return self.query(self.player_id, "rescan")
    
    def getVolume(self, player_id):
        volume = self.query(player_id, "mixer", "volume", "?")
        if len(volume):
            volume = volume['_volume']
        else:
            volume = 0
        return volume
        
    def setVolume(self, player_id, volume):
        self.query(player_id, "mixer", "volume", volume)
        
    def getArtists(self):
        return self.query(self.player_id, "artists", 0, 9999)['artists_loop']
        
    def getArtistsCount(self):
        return len(self.getArtists())
    
    def getRadiosCount(self):
        return self.query(self.player_id, "favorites", "items")['count']
    
    def playRadio(self, player_id, radio):
        return self.query(player_id, "favorites", "playlist", "play", "item_id:"+str(radio))
        
    def getArtistAlbum(self, player_id, artist_id):
        return self.query(player_id, "albums", 0, 99, "tags:al", "artist_id:"+str(artist_id))['albums_loop']
        
    def playAlbum(self, player_id, id):
        return self.query(player_id, "playlistcontrol", "cmd:load", "album_id:"+str(id))
        
    def pause(self, player_id):
        return self.query(player_id, "pause")
    
    def previousSong(self, player_id):
        return self.query(player_id, "playlist", "index", "-1")

    def nextSong(self, player_id):
        return self.query(player_id, "playlist", "index", "+1")

    def getCurrentSongTitle(self, player_id):
        title = self.query(player_id, "current_title", "?")
        if len(title):
            title = title['_current_title']
        else:
            title = ""
        return title

    def getCurrentArtist(self, player_id):
        artist = self.query(player_id, "artist", "?")
        if len(artist):
            artist = artist['_artist']
        else:
            artist = ""
        return artist

    def getCurrentAlbum(self, player_id):
        album = self.query(player_id, "album", "?")
        if len(album):
            album = album['_album']
        else:
            album = ""
        return album

    def getCurrentTitle(self, player_id):
        title = self.query(player_id, "title", "?")
        if len(title):
            title = title['_title']
        else:
            title = ""
        return title

    def getCurrentRadioTitle(self, player_id, radio):
        return self.query(player_id, "favorites", "items", 0, 99)['loop_loop'][radio]['name']

    def getPlayerCount(self):
        return self.query("", "player", "count", "?")

    def getServerStatus(self):
        return self.query("", "serverstatus", 0, 99)

    def getPlayers(self):
        players = self.query("", "serverstatus", 0, 99)
        if len(players):
            players = players['players_loop']
        return players

    def setPower(self, player_id, power = 1):
        self.query(player_id, "power", power)

    def setPowerAll(self, power = 1):
        players = self.getPlayers()
        for player in players:
            self.setPower(player['playerid'], power)

    def getAlarms(self, player_id, enabled=True):
        if enabled:
            alarmsEnabled = self.getPlayerPref(player_id, "alarmsEnabled")
            if alarmsEnabled == "0":
                return {}
            filter = "enabled"
        else:
            filter = "all"
        return self.query(player_id, "alarms", 0, 99, "filter:%s" % filter)

    def getNextAlarm(self, player_id):
        alarms = self.getAlarms(player_id)
        alarmtime = 0
        delta = 0
        if alarms == {} or alarms['count'] == 0:
            return {}
        for alarmitem in alarms['alarms_loop']:
            if(str((datetime.datetime.today().weekday() + 1) % 7) not in alarmitem['dow']):
                continue
            alarmtime_new = datetime.timedelta(seconds=int(alarmitem['time']))
            now = datetime.datetime.now()
            currenttime = datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
            delta_new = alarmtime_new - currenttime
            if delta == 0:
                delta = delta_new
                alarmtime = alarmtime_new
            elif delta_new < delta:
                delta = delta_new
                alarmtime = alarmtime_new
        if alarmtime == 0:
            return {}
        else:
            return { "alarmtime" : alarmtime.seconds, "delta" : delta.seconds }

    def getPlayerPref(self, player_id, pref):
        return self.query(player_id, "playerpref", pref, "?")['_p2']

    def setPlayerPref(self, player_id, pref, value):
        self.query(player_id, "playerpref", pref, value)
    
    def display(self, player_id, line1, line2, duration = 5):
        self.query(player_id, "display", line1, line2, duration)
        
    def displayAll(self, line1, line2, duration = 5):
        players = self.getPlayers()
        for player in players:
            self.display(player['playerid'], "display", line1, line2, duration)
            
