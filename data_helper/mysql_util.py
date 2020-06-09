import pymysql

db_conn = ""
cursor = ""


def conn(ip, user, password, data):
    global db_conn, cursor
    try:
        db_conn = pymysql.connect(host=ip, user=user, passwd=password, db=data)
        cursor = db_conn.cursor()
    except:
        print("数据库连接失败！")
    return cursor


def query_one(cursor, sql):
    cursor.execute(sql)
    results = cursor.fetchone()
    for items in results:
        return items[0]


def query_two(cursor, sql):
    cursor.execute(sql)
    config_lsit = {}
    results = cursor.fetchall()
    for items in results:
        config_lsit[items[0]] = items[1]
    return config_lsit


def close():
    global cursor, db_conn
    cursor.close()
    db_conn.close()
