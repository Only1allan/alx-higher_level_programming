#!/usr/bin/python3
"""
a script takes in the name of state and lists all cities of state
"""
import MySQLdb
import sys

if __name__ == '__main__':
    database = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3],
            port=3306
        )
    cursor = database.cursor()
    match = sys.argv[4]
    query = "SELECT cities.name \
                    FROM cities\
                    INNER JOIN states ON (states.id = cities.state_id)\
                    WHERE state.name=%s \
                    ORDER BY states.id"
    cursor.execute(query, (sys.argv[4], ))
    cities = cursor.fetchall()

    city_names = [city[0]for city in cities]
    city_total = ", ".join(city_names)
    print(city_total)

    cursor.close()
    database.close()
