import pandas as pd
from config import *

def create_state_dataset():

    data = pd.read_csv(CLEANED_DATA_DIR)
    df = data.copy(deep=True)
    df = df.groupby(['State name']).mean(numeric_only=True)
    df.to_csv('data/cleaned/US_States_Health_Stats.csv')