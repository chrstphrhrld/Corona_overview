from main import *
import requests

# Klasse Calculation
class Calculation():
    '''Alle Berechnungen laut Aufgabenstellung'''

# Konstruktor für Klasse Calculation
    def __init__(self, request):
        self.Request = request
        self.Population = self.currentPopulation()

# Aufgabe II Funktion um die Infektionsrate zu Vortag zu Berechnen
    def getInfektionRate(self):
        '''Funktion zur Berechnung Aktiver Fälle und die jeweilige Infektionsrate zum Vortag
        :return - Gibt für jeden Tag (nach Abfrage) die Aktiven fälle aus,
                - falls keine Vortag zum Vergleich vorhanden ist wird "noch kein Wert" gezeigt
                - in einer For-Schleife wird für jeden Tag die Infektionsrate zum Vortag berechnet'''
        n = 0
        while (len(self.Request.range) > n):
            if n == 0:
                #print("kein Wert", self.Request.range[n]['Active'])
                self.Request.range[n]["Daily_infektion_rate"] = "kein Wert"
            else:
                self.Request.range[n]["Daily_infektion_rate"] = round((self.Request.range[n]['Active'] * 100 / self.Request.range[n - 1]['Active']) - 100, 2)
                #print("Aktive Fälle:", self.Request.range[n]['Active'])
            n += 1

        for datensatz in self.Request.range:
            print("Infektionsrate:", datensatz["Daily_infektion_rate"], "%")
        return self.Request.range

# Aufgabe III API für Population in jeweilig angefragten Land
    def currentPopulation(self):
        '''Zieht sich die Daten der Population des gefragten Landes von API
        :return - Populationsdaten in json'''
        url = "https://restcountries.eu/rest/v2/all"
        get_url = requests.get(url)
        data = get_url.json()

        for element in data:
            if element["name"] == self.Request.range[0]["Country"]:
                return element["population"]

# Aufgabe III Population in jeweilig angefragten Land
    def recoveredRatio(self):
        '''Berechnet die Genesene Bevölkerung
        :return - Daten für Genesene Bevölkerung pro Tag'''
        population_size = self.Population
        ratio = round(100 / population_size * self.Request.range[-1]['Recovered'], 2)
        print("Genesene Bevölkerung", ratio, "%")
        return ratio

# Aufgabe IV
    def infektedRatio(self):
        '''Berechnet die infizierten Anzahl
        :return - infizierten Anzahl
                - gibt eine Warnung wenn Wert über 0,01%'''
        population_size = self.Population
        ratio = round(100 / population_size * self.Request.range[-1]['Active'], 2)
        print("Es sind", ratio, "% der Bevölkerung des Landes sind aktuell infiziert")
        if (ratio > 0.01):
            print("WARNUNG!!!")
        return ratio

# PR test def
    def calcCoolStuff(self):
        myInt = 100
        myDec = 0,59
        if myInt > myDec:
            return myInt / myDec

# Für Test:

#calculation = Calculation(abfrage)
#calculation.getInfektionRate()
#print("")
#calculation.recoveredRatio()
#print("")
#calculation.infektedRatio()
