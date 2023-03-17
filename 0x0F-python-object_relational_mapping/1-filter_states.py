#!/usr/bin/python3

"""
Lists all states from the states table of database hbtn_0e_0_usa.
Usage: ./0-select_states.py <username> \
                            <password> \
                             <database-name>
"""
import sys
import MySQLdb as db


def connect_and_query() -> None:

    """Connect to the database and execute query
    filter only states that start with `N` 
    """
    try:
        cnx = db.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = cnx.cursor(cursorclass=db.cursors.Cursor)
        cursor.execute("SELECT * FROM states WHERE name IN ('Nevada', 'New York')  ORDER BY `id` ASC;")
        states = cursor.fetchall()

        for state in states:
            print(state)
    except Exception as e:
        return (e)


if __name__ == "__main__":
    connect_and_query()
