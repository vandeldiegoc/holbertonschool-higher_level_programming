#!/usr/bin/python3
"""conect database to python code"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]
    sql = "SELECT * FROM states WHERE name='{}'ORDER BY id ASC".format(name)
    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=passwd, db=db, charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == name:
            print(row)
    cur.close()
    conn.close()
