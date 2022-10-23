from insert_statements import insert_admin_type
import mysql.connector as conn
from config import config
import datetime

# connection
def connectdb():
    params = config()
    connection = conn.connect(**params)
    
    return connection

connection = connectdb()
cur = connection.cursor()
insert_ = insert_admin_type()
insert_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def insert_data():
    admin_type = 'state'
    data = (admin_type,insert_date)

    cur.execute(insert_,data)
    connection.commit()
    connection.close()

def run():
    insert_data()

if __name__ == "__main__":
    run()
