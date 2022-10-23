from read_files import get_admin_2
from insert_statements import insert_admin_2
import mysql.connector as conn
from config import config

# connection
def connectdb():
    params = config()
    connection = conn.connect(**params)
    
    return connection

connection = connectdb()
cur = connection.cursor()
df = get_admin_2()
insert_ = insert_admin_2()

# df['values'] = df[['value1', 'value2', 'value3']].values.tolist()
def by_row():
    df['data'] = df[['admin_name','admin_type','pais_id']].values.tolist()
    rows = list(df['data'])
    return rows

def insert_admin_2():
    data_list = []
    lists = by_row()

    for data in lists:
        data_list.append(tuple(data)) 

    #return data_list
    cur.executemany(insert_,data_list)
    connection.commit()
    connection.close()

def run():
    insert_admin_2()


if __name__ == "__main__":
    run()