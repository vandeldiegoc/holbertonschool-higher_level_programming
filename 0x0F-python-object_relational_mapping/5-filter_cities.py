#!/usr/bin/python3
"""conect database to python code"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]
    sql = "SELECT cities.name FROM states \
           INNER JOIN cities ON states.id = cities.state_id \
           WHERE states.name=%s ORDER BY cities.id ASC"
    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=passwd, db=db, charset="utf8")
    cur = conn.cursor()
    cur.execute(sql, (name,))
    query_rows = cur.fetchall()
    list = []
    for row in query_rows:
        list.append(row[0])
    print(", ".join(list))
    cur.close()
    conn.close()
