#/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":

	if len(sys.argv) != 4:
		print("Missing arguments")
		sys.exit(1);

	db = MySQLdb.connect(
		host="localhost",
		port = 3306,
		user=sys.argv[1],
		passwd=sys.argv[2],
		db=sys.argv[3])

	cur = db.cursor()

	query = "SELECT * FROM states ORDER BY states.id"
	cur.execute(query)

	results = cur.fetchall()
	for row in results:
		print(row)

	cur.close()
	db.close()
