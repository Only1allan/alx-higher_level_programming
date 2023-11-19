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

    query = "SELECT * FROM states \
        WHERE CONVERT(`name` USING Latin1) \
        COLLATE Latin1_General_CS \
     LIKE 'N%' ORDER BY states.id ASC"
    cur.execute(query)

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()
