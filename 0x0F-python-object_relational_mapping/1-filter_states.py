#!/usr/bin/python3
"""
all states with a name starting with N from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],

        db=sys.argv[3])

    cur = db.cursor()

    query = "SELECT id, name FROM states \
        WHERE name LIKE 'N%' ORDER BY states.id "
    cur.execute(query)

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()
