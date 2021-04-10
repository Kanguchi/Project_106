import pandas as pd
import plotly.express as px
import csv
import numpy

def get_data_source(data_path):
    dayspresent = []
    marksinpercentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            dayspresent.append(float(row['Days Present']))
            marksinpercentage.append(float(row['Marks In Percentage']))
    return {'x': dayspresent, 'y': marksinpercentage}

def find_correlation(data_source):
    correlation = numpy.corrcoef(data_source['x'], data_source['y'])
    print("The Correlation between Attendance and Marks is: \n-->", correlation[0, 1])

def setup():
    data_path = 'rollvmarks.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()

df = pd.read_csv('rollvmarks.csv')
fig = px.scatter(df, x = 'Days Present', y='Marks In Percentage')
fig.show()

