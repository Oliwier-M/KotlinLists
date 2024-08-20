from disease import Disease
import csv
from matchDieaseses import matching_diseases

with open("InfectiousDiseases.csv") as f:
    content = csv.reader(f, delimiter=';')

    diseases = []

    for row in content:
        d = Disease(row[0], row[1], row[2], row[3], row[4])
        diseases.append(d)

