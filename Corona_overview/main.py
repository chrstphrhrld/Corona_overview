import requests
from datetime import timedelta
import datetime
from database import *

# Klasse Request
class Request():
    '''Stellt eine Anfrage an die API und holt Daten'''

# Konstruktor für Klasse Request
# "number_of_days" default auf 6 (für 7 Tage wegen 0-6)
    def __init__(self, country, number_of_days=6):
        self.Country = country
        self.Number_of_Days = number_of_days
        self.Data = self.getinfo()
        self.range = self.getRange()

# Funktion für API Request
    def getinfo(self):
        '''Zieht die Daten aus der covid 19 api
        :return - json Daten der api'''
        covid_url = "https://api.covid19api.com/total/dayone/country/"
        api_url = covid_url + self.Country
        get_url = requests.get(api_url)
        data = get_url.json()
        return data

# Funktion für Abfrage der Tage und Eingrenzung auf Eingabewert ("Tage")
    def getRange(self):
        '''Grenzt die Tage auf den jeweilig eingegebenen Wert ein
        :return - Daten in Tagesfolge nach abfrage'''
        time_today = datetime.date.today()
        delta = time_today - timedelta(days=self.Number_of_Days + 1)
        date_span = []
# Checkt ob sich das Datum im Zeitraum befindet
        for day in self.Data:
            if(str((day['Date']).split("T")[0]) > str(delta)):
                date_span.append(day)
        return date_span

# Aufgabe I Visualisierung
    def printData(self):
        '''Print Befehl für Terminal und Vorverarbeitung für GUI
        :return - active, confirmed, deaths, dates, recovered'''
        print("Land:", self.range[0]['Country'])
        active = []
        confirmed = []
        deaths = []
        dates = []
        recovered = []
        database = Database()
        for day in self.range:
            active.append(day['Active'])
            confirmed.append(day['Confirmed'])
            deaths.append(day['Deaths'])
            recovered.append(day['Recovered'])
            dates.append((day["Date"]).split("T")[0][5:])
            print("Datum:", (day["Date"]).split("T")[0],"Aktive Fälle:", day['Active'],"Bestätigte Fälle:", day['Confirmed'], "Es sind gestorben:", day['Deaths'], "Es sind genesen:", day['Recovered'])
            database.insertInDb(dates, active, confirmed, deaths, recovered)
        return {"active": active, "confirmed": confirmed, "deaths": deaths, "recovered": recovered, "dates": dates}


# Für Test:

abfrage = Request("Germany")
abfrage.printData()
