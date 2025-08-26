#les10 vraag4
from helper import *
#les10 vraag9
from presentatie import presenteer
#les10 vraag11
import csv

#les10 vraag2
inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

#les10 vraag5
print(som(inkomsten))

#les10 vraag10
totaal = som(inkomsten)
presenteer(inkomsten, totaal)

#les10 vraag12
with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key, value])


