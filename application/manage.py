import os
from psycopg2 import connect


class Database(object):

    def __init__(self, app_config):
        self.dbname = app_config.get('DATABASE_NAME')
        self.user = app_config.get('USER')
        self.password = app_config.get('PASSWORD')
        self.host = app_config.get('HOST')
        print("...Establishing connection to database server...")
        self.connection = connect(
            database=self.dbname, user=self.user, host=self.host, password=self.password)
        self.connection.autocommit = True
        print("Connected.")

    def create_all(self):
        print("... starting creation of relations")
        commands = (
            'CREATE TABLE IF NOT EXISTS users (user_id serial PRIMARY KEY, \
                        firstname varchar(255), \
                        secondname varchar(255), \
                        email varchar(50) NOT NULL, \
                        password varchar(255) NOT NULL, \
                        phone varchar(255) NOT NULL, \
                        UNIQUE(email))',

            'CREATE TABLE IF NOT EXISTS entries (entry_id serial PRIMARY KEY, \
                       owner_id serial, \
                       title varchar(255), \
                       body varchar(255), \
                       date_created varchar(255), \
                       date_modified varchar(255), \
                       FOREIGN KEY (owner_id) REFERENCES users(user_id) on delete cascade)'
        )

        try:
            cursor = self.connection.cursor()
            # create table one by one
            print("Creating relations")
            for command in commands:
                cursor.execute(command)
            # close communication with the PostgreSQL database server
            cursor.close()
            print("Done.")
        except (Exception) as error:
            print(error)

    def drop_all(self):
        commands = (
            'DROP TABLE "users" CASCADE',
            'DROP TABLE "entries" CASCADE'
        )
        try:
            cursor = self.connection.cursor()
            # drop table one by one
            print("Deleting relations")
            for command in commands:
                cursor.execute(command)
            # close communication with the PostgreSQL database server
            cursor.close()
            print("Done.")
        except (Exception) as error:
            print(error)

    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor

    def __del__(self):
        #close connection to the database / destroy an instance of the class
        self.connection.close()
