import json
import csv

datos = json.load(open('pliego.json'))

w = csv.DictWriter(open('pliego.csv', 'w'), fieldnames=datos[0].keys())
w.writeheader()
w.writerows(datos)


