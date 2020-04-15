import plotly
import csv
from collections import namedtuple

# This is a list of the thinks I could do to the data:
# TODO: Get a plot of the result of the age of the patient
#       and the respiratory syncytial virus. I'm trying to use a histogram.


name_file = 'diagnosis-of-covid-19-and-its-clinical-spectrum.csv'
with open('headers.txt', 'r') as f:
    headers = f.readline().strip().split(',')
data = []
Case = namedtuple('Case', headers)


def init():
    with open(name_file, 'r') as f:
        reader = csv.DictReader(f)
        data.clear()
        for row in reader:
            case = create_case(row)
            data.append(case)


def create_case(row):
    row['patient_age'] = int(row['patient_age']) * 5
    case = Case(
        **row
    )
    return case


if __name__ == '__main__':
    init()
    print(data[1])
