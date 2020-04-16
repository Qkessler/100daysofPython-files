import plotly.graph_objects as go
import csv
from collections import namedtuple

# This is a list of the thinks I could do to the data:
# DONE: Get a plot of the result of the age of the patient
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


def negative_data():
    negative_data = {}
    for case in data:
        if case.sars_cov_2_exam_result == 'negative':
            if case.patient_age not in negative_data.keys():
                negative_data[case.patient_age] = 1
            else:
                negative_data[case.patient_age] += 1
    negative_data = sorted(negative_data.items(), key=lambda item: item[0])
    return transpose_tuples(negative_data)


def positive_data():
    positive_data = {}
    for case in data:
        if case.sars_cov_2_exam_result == 'positive':
            if case.patient_age not in positive_data.keys():
                positive_data[case.patient_age] = 1
            else:
                positive_data[case.patient_age] += 1
    positive_data = sorted(positive_data.items(), key=lambda item: item[0])
    return transpose_tuples(positive_data)


def get_fig(pos_x, pos_y, neg_x, neg_y):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=pos_x, y=pos_y, name='Positive cases'))
    fig.add_trace(go.Bar(x=neg_x, y=neg_y, name='Negative cases'))
    fig.update_layout(barmode='stack')
    return fig


if __name__ == '__main__':
    init()
    pos_x, pos_y = positive_data()
    neg_x, neg_y = negative_data()
    fig = get_fig(pos_x, pos_y, neg_x, neg_y)
    fig.show()
