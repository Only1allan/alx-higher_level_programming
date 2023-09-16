#!/usr/bin/python3
"""
script listing all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    database = MySQLdb.connect(
        user=sys.argv[1],
        passwd = sys.argv[2],
        database = sys.argv[3],
        port=3306
    )
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    states = cursor.fetchall()

    for state in states:
        print(state)