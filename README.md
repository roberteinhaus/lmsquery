# LMSQuery
**Query library for Logitech Media Server**

This library provides easy to use functions to send queries to a Logitech Media Server (https://github.com/Logitech/slimserver)

### Usage Example
    import lmsquery
    lms = lmsquery.LMSQuery('127.0.0.1', '9000') # user ip and port of lms server
    players = lms.getPlayers()
    for player in players:
      print player['name']
