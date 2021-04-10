import pandas as pd
import plotly.express as px
import numpy as np
import csv

def get_data_source(data_path):
    amountofcoffee = []
    sleepinhours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            amountofcoffee.append(float(row['Coffee in ml']))
            sleepinhours.append(float(row['sleep in hours']))
    return {'x': amountofcoffee, 'y': sleepinhours}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print("The Correlation between Coffe Consumption and Amount of Sleep is: \n-->", correlation[0, 1])

def setup():
    data_path = 'coffeevsleep.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()

df = pd.read_csv('coffeevsleep.csv')
fig = px.scatter(df, x = 'Coffee in ml', y = 'sleep in hours')
fig.show()