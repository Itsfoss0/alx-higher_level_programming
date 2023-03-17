#!/usr/bin/python3

"""
Lists all states from the states table of database hbtn_0e_0_usa.
Usage: ./0-select_states.py <username> \
                            <password> \
                             <database-name>
"""
import sys
import MySQLdb as db

[USERNAME, PASSWORD, DB_NAME] = sys.argv[1:4]


if __name__ == "__main__":
    try:
        cnx = db.connect(user=USERNAME, passwd=PASSWORD, db=DB_NAME)
        cursor = cnx.cursor(cursorclass=db.cursors.Cursor)
        cursor.execute('SELECT * FROM states ORDER BY `id` ASC;')
        states = cursor.fetchall()

        for state in states:
            print(state)
    except Exception as e:
        print(e)
    finally:
        cnx.close()
        cursor.close()
