#!/usr/bin/env python3

import sqlite3

def main():
    pos = (0,0)
    cableNo = 0
    with open('input.txt') as f:
        input = [line.rstrip('\n').split(',') for line in f]

    try:
        sqliteConnection = sqlite3.connect('day3-p1.db')
        cursor = sqliteConnection.cursor()

        for table in ('cable0', 'cable1'):
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {table} (cable_type INTEGER NOT NULL, x_coordinate INTEGER NOT NULL, y_coordinate INTEGER NOT NULL);')

        for mv in input[0]:
            for _ in range(int(mv[1:])):
                if mv[0] == 'R':
                    pos = (pos[0]+1, pos[1])
                elif mv[0] == 'L':
                    pos = (pos[0]-1, pos[1])
                elif mv[0] == 'U':
                    pos = (pos[0], pos[1]+1)
                elif mv[0] == 'D':
                    pos = (pos[0], pos[1]-1)
                cursor.execute(f'INSERT INTO cable0 (cable_type, x_coordinate, y_coordinate) values ({cableNo}, {pos[0]}, {pos[1]})')

        cableNo += 1
        pos = (0,0)
        
        for mv in input[1]:
            for _ in range(int(mv[1:])):
                if mv[0] == 'R':
                    pos = (pos[0]+1, pos[1])
                elif mv[0] == 'L':
                    pos = (pos[0]-1, pos[1])
                elif mv[0] == 'U':
                    pos = (pos[0], pos[1]+1)
                elif mv[0] == 'D':
                    pos = (pos[0], pos[1]-1)
                cursor.execute(f'INSERT INTO cable1 (cable_type, x_coordinate, y_coordinate) values ({cableNo}, {pos[0]}, {pos[1]})')

        sqliteConnection.commit()

        cursor.execute("""SELECT min(abs(cable0.x_coordinate) + abs(cable0.y_coordinate)) 
                        from cable0 inner join cable1 
                        on cable0.x_coordinate=cable1.x_coordinate 
                        and cable0.y_coordinate=cable1.y_coordinate;""")
        
        print(f'Result: {cursor.fetchone()[0]}')
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

main()