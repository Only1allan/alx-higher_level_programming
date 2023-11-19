#!/usr/bin/python3
"""
 takes in an argument and displays states in table of hbtn_0e_0_usa .
"""
import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Missing right no of arguments")
        sys.exit(1)

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cur = db.cursor()

    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name = BINARY '{:s}' \
        ORDER BY states.id ASC".format(
        state_name)
    cur.execute(query, (state_name,))

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
