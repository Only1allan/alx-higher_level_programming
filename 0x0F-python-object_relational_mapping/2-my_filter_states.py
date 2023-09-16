#!/usr/bin/python3
"""
script takes argument and displays values in tates where name matches rgument.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Invalid argument number")
        sys.exit(1)
    try:
        search_state = sys.argv[4],
        database = MySQLdb.connect(
                user=sys.argv[1],
                passwd=sys.argv[2],
                database=sys.argv[3],
                port=3306
            )
        cursor = database.cursor()
        query = "SELECT * \
                        FROM states\
                        WHERE name = %s \
                        ORDER BY states.id"
        cursor.execute(query, (search_state,))
        states = cursor.fetchall()

        for state in states:
            print(state)
    except MySQLdb.Error as error:
        print("Could not connect to server")

    finally:
        cursor.close()
        database.close()
