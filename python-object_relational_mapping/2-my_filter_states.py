#!/usr/bin/python3
"""
doc
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC".format(state_name_searched)
    cursor.execute(query, (state_name_searched,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
