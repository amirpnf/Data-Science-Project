import pandas as pd

def clean_dataset(path):

    df = pd.read_csv(path)
    df = df.rename(columns = {
        'TotalPopulation' : 'Total Population',
        'StateDesc' : 'State name',
        'TotalPop18plus' : 'Total adult population'
    })
    df.to_csv('data/cleaned/US_Counties_Health_Stats_CLEANED.csv', header=True, index=False)