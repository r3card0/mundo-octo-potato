def insert_continents():
    insert_ = "INSERT INTO continents(continent_name,insert_date) VALUES(%s,%s)"
    return insert_


def insert_countries():
    insert_ = "INSERT INTO countries(country_name,continent_id) VALUES(%s,%s)"
    return insert_


def insert_continent_zones():
    insert_ = "INSERT INTO continent_zones(zone_name,continent_id) VALUES(%s,%s)"
    return insert_

def insert_admin_type():
    insert_ = "INSERT INTO admin_types(admin_type,insert_date) VALUES(%s,%s)"
    return insert_

def insert_admin_2():
    insert_ = "INSERT INTO admin2(admin2_name,admin_type,country_id) VALUES(%s,%s,%s)"
    return insert_