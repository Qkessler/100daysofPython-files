from openpyxl import load_workbook
from collections import Counter


def init_spreadsheet(recurso):
    wb = load_workbook(recurso)
    return wb['Finances 2017']


# To test the skills, I will try to get a counter going for the countries.
# Getting 10 most common countries.
def count_countries(spreadsheet):
    countries = []
    for row in list('B'):
        for col in range(2, 701):
            cell = row + str(col)
            countries.append(spreadsheet[cell].value)
    c = Counter(countries)
    return c.most_common(10)


if __name__ == '__main__':
    ws1 = init_spreadsheet('../code/Financial Sample.xlsx')
    dictionary = count_countries(ws1)
    print(dictionary)
