import pymysql

# MySQL 데이터베이스 연결
MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='root', 
    password='tmdgml852756!',
    db='mypage', 
    charset='utf8')

def conn_mysqldb():
    return MYSQL_CONN
