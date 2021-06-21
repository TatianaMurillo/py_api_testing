from py_api_test.src.utilities.DbUtility import DBUtility


class CustomerDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users where user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

