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
    query = "SELECT DISTINCT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE states.name=%s"
    cur.execute(query, (state_name,))
    results = cur.fetchall()

    print(", ".join([row[0] for row in results]))

    cur.close()
    db.close()
