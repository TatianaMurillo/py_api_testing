
from py_api_test.src.configs.db_credentials import CREDENTIALS as DB_CREDENTIALS
from py_api_test.src.woocredentials.woo_credentials import CREDENTIALS as WOO_CREDENTIALS


class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():

        wc_key = WOO_CREDENTIALS["wc_key"]
        wc_secret = WOO_CREDENTIALS["wc_secret"]

        if not wc_key or not wc_secret:
            raise Exception("The API credentials 'WC_KEY' and 'WC_SECRET' must be in env variable")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_credentials():
        db_user = DB_CREDENTIALS["db_user"]
        db_password = DB_CREDENTIALS["db_password"]
        db_socket = DB_CREDENTIALS["db_socket"]
        db_host = DB_CREDENTIALS["db_host"]

        if not db_user or not db_password:
            raise Exception("The DB credentials must be in env variables")
        else:
            return {'db_user': db_user, 'db_password': db_password, 'db_socket': db_socket, 'db_host': db_host}