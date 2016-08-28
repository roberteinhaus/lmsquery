import const
import lmsquery

def LMSQuery(host=const.LMS_HOST, port=const.LMS_PORT, player_id=""):
    return lmsquery.LMSQuery(host, port, player_id)
