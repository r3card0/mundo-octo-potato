from connect import connectdb, close_connection
import pandas as pd
import datetime

# global variables
connection = connectdb()
cur = connection.cursor()
insert_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# def zones_01():
#     zone_list = ['North America','South America','Middle East','Eastern Europe','Western Europe','Northern Europe','Southern Europe','Central Europe']
#     continent_id_list = [1,1,3,6,6,6,6,6]
#     zone_dict01 = {
#         "zone_name_list" : zone_list,
#         "continent_id_list" : continent_id_list,
#     }
#     return zone_dict01

def zones_01():
    zone_tuple_list =[('North America',1), ('South America',1),('Middle East',3)]
    return zone_tuple_list


def insert_data():
    data = zones_01()
    insert_ = "INSERT INTO continent_zones(zone_name,continent_id) VALUES(%s,%s)"
    # for continent in continents_list:
    #     data.append(tuple((continent,insert_date)))

    #return data
    cur.executemany(insert_,data)
    connection.commit()
    connection.close()


def run():
    insert_data()


if __name__ == "__main__":
    run()