#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage:
------
./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

# 1st command-line argument would return the filename that was run
USER = sys.argv[1]  # 1st command-line argument after executable
PASSWORD = sys.argv[2]  # 2nd command-line argument after executable
DB_NAME = sys.argv[3]  # 3rd command-line argument after executable

if __name__ == "__main__":
    db = MySQLdb.connect(user=USER, passwd=PASSWORD, db=DB_NAME)
    cur = db.cursor()

    cur.execute("SELECT * from states where name like 'N%';")
    result = cur.fetchall()
    [print(state) for state in result]
