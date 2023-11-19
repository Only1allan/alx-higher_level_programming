#!/usr/bin/python3
"""
takes in name of a state as an argument and lists all cities of that state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    state_name = sys.argv[4]

    cur = db.cursor()
    query = "SELECT * FROM cities WHERE name=%s ORDER BY cities.id"
    cur.execute(query, (state_name,))
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
