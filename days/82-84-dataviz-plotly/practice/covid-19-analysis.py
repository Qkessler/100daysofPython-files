import plotly.graph_objects as go
import csv
from collections import namedtuple

# This is a list of the thinks I could do to the data:
# TODO: Get a plot of the result of the age of the patient
#       and the sars_cov_exam. The idea is to get the number
#       with and without it per age. Maybe get two histograms
#       one with and one without.


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


def transpose_tuples(data):
    if isinstance(data, dict):
        data = data.items()
    transposed = list(zip(*data))
    return transposed


def data_age_syncytial():
    data_dict = {case.patient_age:case.respiratory_syncytial_virus
                 for case in data if case.respiratory_syncytial_virus}
    return transpose_tuples(data_dict)


if __name__ == '__main__':
    init()
    x, y = data_age_syncytial()
    print(x, y)
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.show()
