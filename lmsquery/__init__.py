import constants
import lmsquery

def LMSQuery(host=constants.LMS_HOST, port=constants.LMS_PORT, player_id=""):
    return lmsquery.LMSQuery(host, port, player_id)
