import configparser
from pathlib import Path
import  pymysql

_CONFIG_PATH = Path(__file__).parent.parent / 'config'/"db_config.ini"

def get_config():
    parser = configparser.ConfigParser()
    parser.read(_CONFIG_PATH,encoding='utf-8')
    return parser["mysql"]

def query(sql,params = None):
    c = get_config()
    conn = pymysql.connect(
        host=c["host"],
        port=int(c["port"]),
        user=c["user"],
        password=c["password"],
        database=c["database"],
        charset=c["charset"],
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with conn.cursor() as cur:
            cur.execute(sql,params)
            return cur.fetchall()
    finally:
        conn.close()
