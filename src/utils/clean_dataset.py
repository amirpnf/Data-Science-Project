import pandas as pd

def clean_dataset(path):

    df = pd.read_csv(path)

    df = df.rename(columns = {
        'TotalPopulation' : 'Total Population',
        'StateDesc' : 'State name',
        'TotalPop18plus' : 'Total adult population',
        'OBESITY_CrudePrev': 'Obesity Prevalence (%)',
        'CANCER_CrudePrev': 'Cancer Prevalence (%)',
        'STROKE_CrudePrev': 'Stroke Prevalence (%)',
        'ARTHRITIS_CrudePrev': 'Arthritis Prevalence (%)',
        'DEPRESSION_CrudePrev': 'Depression Prevalence (%)',
        'DIABETES_CrudePrev': 'Diabetes Prevalence (%)',
        'HIGHCHOL_CrudePrev': 'High Cholesterol Prevalence (%)',
        'TEETHLOST_CrudePrev': 'Teeth Lost Prevalence (%)'
    })
    df['CountyName'] = df['CountyName'].replace('DoÃ±a Ana', 'Doña Ana')
    df.to_csv('data/cleaned/US_Counties_Health_Stats_Cleaned.csv', header=True, index=True)