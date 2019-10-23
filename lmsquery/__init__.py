from . import const
from . import lmsquery
from .scanLMS import scanLMS

def LMSQuery(host=const.LMS_HOST, port=const.LMS_PORT, player_id=""):
    return lmsquery.LMSQuery(host, port, player_id)
