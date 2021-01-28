from main import *
import os
import sqlite3

# Aufgabe V Daten in SQLite-Tabelle Speichern
PATH = os.path.join(os.path.dirname(__file__), 'database_api.sqlite3')

# Klasse Database
class Database():
    '''Datenbank für covid Daten'''

# Konstruktor für Datenbank
    def __init__(self):
        '''Stellt Verbindung zur Datenbank her,
        erstellt eine Datenbankdatei wenn nicht vorhanden'''
        self.connection = sqlite3.connect(PATH)
        try:
            self.newDb()
        except sqlite3.OperationalError:
            pass

# Funktion für neue Datenbank
    def newDb(self):
        '''Ersellte eine Tabelle für covid Einträge'''
        cursor = self.connection.cursor()
        query = f'''
            CREATE TABLE covid_status (
                id INTEGER PRIMARY KEY,
                dates VARCHAR(200),
                active VARCHAR(200),
                confirmed VARCHAR(200),
                deaths VARCHAR(200),
                recovered VARCHAR(200)
            );
            '''
        cursor.execute(query)
        self.connection.commit()

# Funktion für Insert in die Datenbank
    def insertInDb(self, dates, active, confirmed, deaths, recovered):
        '''benötigt: dates, active, confirmed, deaths, recovered aus "main" - "printData"
         :return - Daten in SQLite3 Datenbank'''
        cursor = self.connection.cursor()
        for val in range(0, len(dates)):
            insert_query = f'''
                INSERT INTO covid_status (id, dates, active, confirmed, deaths, recovered)
                VALUES (NULL, "{dates[val]}", "{active[val]}", "{confirmed[val]}", "{deaths[val]}", "{recovered[val]}");
                '''
            cursor.execute(insert_query)
        self.connection.commit()

database = Database()
