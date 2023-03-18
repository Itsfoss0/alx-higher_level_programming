#!/usr/bin/python3

"""
Lists all cities from the cities table of database hbtn_0e_0_usa.
Usage: ./0-select_states.py <username> \
                            <password> \
                             <database-name>
"""
import sys
import MySQLdb as db


def connect_and_query() -> None:

    """Connect to the database and execute query"""
    try:
        cnx = db.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = cnx.cursor(cursorclass=db.cursors.Cursor)
        cursor.execute('SELECT city.id, city.name, state.name\
                        FROM cities as city\
                        INNER JOIN states as state\
                        ON city.state_id = %s\
                        ORDER BY city.id ASC;', sys.argv[4].id)
        cities = cursor.fetchall()

        for city in cities:
            if city[2] == sys.argv[4]:
                print(city)

        cursor.close()
        cnx.close()
    except Exception as e:
        return (e)


if __name__ == "__main__":
    connect_and_query()
