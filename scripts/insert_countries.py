from read_files import get_countries
from insert_statements import insert_countries
import mysql.connector as conn
from config import config

# connection
def connectdb():
    params = config()
    connection = conn.connect(**params)
    
    return connection

connection = connectdb()
cur = connection.cursor()
df = get_countries()
insert_ = insert_countries()

# df['values'] = df[['value1', 'value2', 'value3']].values.tolist()
def by_row():
    df['data'] = df[['pais','continente']].values.tolist()
    rows = list(df['data'])
    return rows

def insert_countries():
    data_list = []
    lists = by_row()

    for data in lists:
        data_list.append(tuple(data)) 

    cur.executemany(insert_,data_list)
    connection.commit()
    connection.close()

def run():
    #print(by_row())
    #print(insert_countries())
    insert_countries()


if __name__ == "__main__":
    run()