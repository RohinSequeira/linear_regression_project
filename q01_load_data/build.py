# %load q01_load_data/build.py
# Default imports
import pandas as pd

path = 'data/house_prices_multivariate.csv'



def load_data(path):
    data = pd.read_csv(path)
    return data
