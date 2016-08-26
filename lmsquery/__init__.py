import lmsquery

def LMSQuery(host="127.0.0.1", port=9000, player_id=""):
    return lmsquery.LMSQuery(host, port, player_id)