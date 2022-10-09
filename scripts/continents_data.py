from connect import connectdb, close_connection
import pandas as pd
import datetime

# global variables
connection = connectdb()
cur = connection.cursor()
insert_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def continents():
    continents_list = ['America','Africa','Asia','Antartica','Oceania','Europe']
    return continents_list

def insert_data():
    continents_list = continents()
    data = []
    insert_ = "INSERT INTO continents(continent_name,insert_date) VALUES(%s,%s)"
    for continent in continents_list:
        data.append(tuple((continent,insert_date)))

    # return data
    cur.executemany(insert_,data)
    connection.commit()
    connection.close()
    
def select_statement():
    select ="""
    SELECT * FROM continents
    """
    return select

def data_table():
    df = pd.read_sql_query(select_statement(),connection)
    return df

def run():
    # print(insert_data())
    insert_data()
    print(data_table())
    print(close_connection())


if __name__ == "__main__":
    run()