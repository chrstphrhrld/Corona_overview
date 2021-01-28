from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from calculation import *

# GUI Corona overview

# Initalisierung des GUI Fensters
root = Tk()
root.title('Corona Daten')
root.geometry("620x800")
corona_img = ImageTk.PhotoImage(Image.open("corona.jpg"))
header = Label(image=corona_img, height=200)
header.pack()


# Funktion für Grafischedarstellung der gefragten Werte
def showData(country):
    '''root für gefragte werte in GUI, braucht Land als eingabe
    :return - Genesene Bevölkerung
            - Infizierte Bevölkerung
            - Daten in Listbox'''
# Tages- und Landabfrage
    days_span = int(days_input.get())
    request = Request(country, days_span)

# Anzeige Genesene Bevölkerung
    recovered = Calculation(request).recoveredRatio()
    recovered_ratio = Label(root, text=f"Genesene Bevölkerung: {recovered} %", fg='blue')
    recovered_ratio.config(font=('Arial', 10, 'bold'))
    recovered_ratio.place(x=35, y=515)

# Anzeige Infizierte Bevölkerung mit Warnung wenn über 0,01%
    infekted = Calculation(request).infektedRatio()
    infekted_ratio = Label(root, text=f"Infizierte Bevölkerung:  {infekted} %", fg='blue')
    infekted_ratio.config(font=('Arial', 10, 'bold'))
    infekted_ratio.place(x=35, y=530)
    if infekted > 0.01:
        warning = Label(root, text=f"WARNUNG, HOHE INFEKTIONSRATE!!!", fg='red')
        warning.config(font=('Arial', 16, 'bold'))
        warning.place(x=250, y=520)

# Daten in Listbox Ausgeben
    data = request.range
    for day in data:
        listbox.insert(END, f" {(day['Date']).split('T')[0]}       |       {day['Confirmed']}       |       {day['Active']}       |       {day['Recovered']}       |       {day['Deaths']}")

# Funktion für Grafischedarstellung
    def drawGraph(dates, values):
        plt.plot(dates, values)
        plt.title("Daten")
        plt.ylabel('Fallzahlen')
        plt.xlabel('Datum')
        plt.show()

    values_for_graphs = request.printData()
    days = values_for_graphs["dates"]

# Buttons für Grafischedarstellung
    button_active = Button(root, text='Aktiv', width=10, command=lambda: drawGraph(days, values_for_graphs["active"]))
    button_active.place(x=20, y=600)

    button_confirmed = Button(root, text='Bestätigt', width=10, command=lambda: drawGraph(days, values_for_graphs["confirmed"]))
    button_confirmed.place(x=170, y=600)

    button_recovered = Button(root, text='Genesen', width=10, command=lambda: drawGraph(days, values_for_graphs["recovered"]))
    button_recovered.place(x=320, y=600)

    button_death = Button(root, text='Tot', width=10, command=lambda: drawGraph(days, values_for_graphs["deaths"]))
    button_death.place(x=470, y=600)

# Tagesabfrage
label_day_request = Label(root, text='Corona Information der letzten x Tage:', fg='blue')
label_day_request.config(font=('Arial', 14, 'bold'))
label_day_request.pack(pady=15)
days_input = Entry(root, width=5)
days_input.pack()

# Länderabfrage
label_country_request = Label(root, text='Länderauswahl:', fg='blue')
label_country_request.config(font=('Arial', 14, 'bold'))
label_country_request.pack(pady=20)

# Buttons für Länderabfrage
button_DE = Button(root, text='Deutschland', width=10, command=lambda: showData("Germany"))
button_DE.place(x=20, y=350)

button_AT = Button(root, text='Österreich', width=10, command=lambda: showData("Austria"))
button_AT.place(x=170, y=350)

button_IT = Button(root, text='Italien', width=10, command=lambda: showData("Italy"))
button_IT.place(x=320, y=350)

button_ES = Button(root, text='Spanien', width=10, command=lambda: showData("Spain"))
button_ES.place(x=470, y=350)

# Lable Spalten Listbox
label_date = Label(root, text='[Datum]', width=10, height=1, fg='blue')
label_date.config(font=('Arial', 12, 'bold'))
label_date.place(x=40, y=400)

label_confirmed = Label(root, text='[Bestätigt]', width=10, height=1, fg='blue')
label_confirmed.config(font=('Arial', 12, 'bold'))
label_confirmed.place(x=170, y=400)

label_active = Label(root, text='[Aktiv]', width=10, height=1, fg='blue')
label_active.config(font=('Arial', 12, 'bold'))
label_active.place(x=275, y=400)

label_recovered = Label(root, text='[Genesen]', width=10, height=1, fg='blue')
label_recovered.config(font=('Arial', 12, 'bold'))
label_recovered.place(x=385, y=400)

label_death = Label(root, text='[Tot]', width=10, height=1, fg='blue')
label_death.config(font=('Arial', 12, 'bold'))
label_death.place(x=490, y=400)

# Listbox für Datenausgabe
listbox = Listbox(root, width=60, height=5)
listbox.pack(pady=80)

root.mainloop()
