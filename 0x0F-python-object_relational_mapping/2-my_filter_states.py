#!/usr/bin/python3
"""conect database to python code"""
import MySQLdb
from sys import argv

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="vda",
                       db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    if row[1] == argv[4]:
        print(row)
cur.close()
conn.close()
