# -*- coding: utf-8 -*-
from sqlite3 import *

"""
    Just a basic setup of all the bot tables.    
"""


class FallenDB:
    __conn = None
    __dbpath = None

    def __init__(self, db_path=None):
        self.__dbpath = db_path

    def __connect(self, db_path):
        self.__dbpath = db_path
        self.__conn = sqlite3.connect(db_path)

    def create_db(self, db_path):
        self.__dbpath = db_path
        self.__connect(db_path)

    def create_table(self):
        if self.__conn is None:
            self.__connect(self.__dbpath)
        try:
            cursor = self.__conn.cursor()
            cursor.executescript('''
            BEGIN TRANSACTION;
            CREATE TABLE IF NOT EXISTS t_config (
                cid INTEGER PRIMARY KEY,
                name text NOT NULL,
                value text NOT NULL,
                date_added DATETIME DEFAULT (DATETIME('now','localtime'))
            );
            COMMIT;
        ''')
        except Error as e:
            print(e)

    def create_setting(self, setting_name: str, setting_value: str) -> None:
        if self.__conn is None:
            self.__connect(self.__dbpath)
        try:
            cursor = self.__conn.cursor()
            cursor.execute("INSERT INTO t_config (cid,name,value,date_added)" \
                               (setting_name, setting_value))
            self.__conn.commit()
            cursor.close()
            return cursor.lastrowid

        except Error as e:
            print(e)

    def delete_setting(self, name: str):
        if self.__conn is None:
            self.__connect(self.__dbpath)
        try:
            cursor = self.__conn.cursor()
            cursor.execute('DELETE FROM t_config WHERE name=?', (name,))
            cursor.close()
        except Error as e:
            print(e)

    def get_setting(self, name: str):
        if self.__conn is None:
            self.__connect(self.__dbpath)
        try:
            curssor = self.__conn.cursor()
            curssor.execute("SELECT cid,name,value,date_added FROM t_config WHERE name=? LIMIT 1;",
                            (name,))
            retVal = curssor.fetchone()
            curssor.close()

        except Error as e:
            retVal = e
        finally:
            return retVal
