#!/usr/bin/python3
"""
script listing all states from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    database = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3],
            port=3306
        )
    cursor = database.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                FROM cities\
                JOIN states ON cities.states_id=states.id\
                ORDER BY cities.id")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    database.close()
