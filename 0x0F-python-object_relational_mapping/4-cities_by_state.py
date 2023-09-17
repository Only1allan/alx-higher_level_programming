#!/usr/bin/python3
"""
script listing all states from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    if len(sys.argv) != 4:
        print("Invalid argument number")
        sys.exit(1)

    try:
        database = MySQLdb.connect(
                user=sys.argv[1],
                passwd=sys.argv[2],
                database=sys.argv[3],
                host="localhost",
                port=3306
            )
        cursor = database.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities\
                    INNER JOIN states ON cities.states_id=states.id \
                    ORDER BY states.id")
        states = cursor.fetchall()

        for state in states:
            print(state)
    except MySQLdb.Error as error:
        print("Could not connect to server")

    finally:
        cursor.close()
        database.close()
