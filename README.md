# LMSQuery
[![PyPI Version](https://img.shields.io/pypi/v/LMSQuery.svg)](https://pypi.python.org/pypi/LMSQuery)
[![PyPI Downloads](https://img.shields.io/pypi/dm/LMSQuery.svg)](https://pypi.python.org/pypi/LMSQuery)
[![Health](https://landscape.io/github/roberteinhaus/lmsquery/master/landscape.svg?style=flat)](https://landscape.io/github/roberteinhaus/lmsquery/master)
    
**Query library for Logitech Media Server**

This library provides easy to use functions to send queries to a Logitech Media Server (https://github.com/Logitech/slimserver)

### Installation
    pip install lmsquery

### Usage Example
    import lmsquery
    lms = lmsquery.LMSQuery('127.0.0.1', '9000') # use ip and port of lms server
    players = lms.get_players()
    for player in players:
      print player['name']
