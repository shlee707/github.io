import re
from model.mysql import conn_mysqldb

class USER:

    def __init__(self, user_id,user_pw):
        self.user_id = user_id
        self.user_pw = user_pw
    
    @staticmethod
    def create(user_id,user_pw):
        db = conn_mysqldb()
        cursor = db.cursor()
        sql = '''INSERT INTO user_table (USER_ID,PW) VALUE ("{0}","{1}")'''.format(user_id,user_pw)
        cursor.execute(sql)
        db.commit()

    @staticmethod
    def find(user_id):
        db = conn_mysqldb()
        cursor = db.cursor()
        sql = '''SELECT * FROM user_table WHERE USER_ID = "{0}"'''.format(user_id)
        cursor.execute(sql)
        user = cursor.fetchone()
        # print('fetchone하면 뭐가나올까',user)
        if not user:
            return None
        user = USER(user[1],user[2])
        return user
    