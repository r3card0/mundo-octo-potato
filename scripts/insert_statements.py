def insert_continents():
    insert_ = "INSERT INTO continents(continent_name,insert_date) VALUES(%s,%s)"
    return insert_


def insert_countries():
    insert_ = "INSERT INTO countries(country_name,continent_id) VALUES(%s,%s)"
    return insert_


def insert_continent_zones():
    insert_ = "INSERT INTO continent_zones(zone_name,continent_id) VALUES(%s,%s)"
    return insert_