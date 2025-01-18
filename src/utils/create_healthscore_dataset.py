import pandas as pd
import os

def create_health_score():

    data = pd.read_csv("data/cleaned/US_Counties_Health_Stats_Cleaned.csv")

    weights = {
        'Obesity Prevalence (%)': 0.3,
        'Cancer Prevalence (%)': 0.2,
        'Stroke Prevalence (%)': 0.15,
        'Arthritis Prevalence (%)': 0.1,
        'Depression Prevalence (%)': 0.1,
        'Diabetes Prevalence (%)': 0.1,
        'High Cholesterol Prevalence (%)': 0.05,
        'Teeth Lost Prevalence (%)': 0.05
    }

    standardized_data = data.copy()
    for column in weights.keys():
        mean = data[column].mean()
        std = data[column].std()
        standardized_data[column] = (mean - data[column]) / std

    weighted_data = standardized_data.copy()
    for column, weight in weights.items():
        weighted_data[column] *= weight

    weighted_data['Health Index'] = weighted_data[list(weights.keys())].sum(axis=1)

    data['Health Index'] = weighted_data['Health Index']

    new_path = 'data/cleaned/Health_Score.csv'
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    data.to_csv(new_path, index=False)

def create_health_score_by_state():
    data = pd.read_csv("data/cleaned/US_States_Health_Stats.csv")

    weights = {
        'Obesity Prevalence (%)': 0.3,
        'Cancer Prevalence (%)': 0.2,
        'Stroke Prevalence (%)': 0.15,
        'Arthritis Prevalence (%)': 0.1,
        'Depression Prevalence (%)': 0.1,
        'Diabetes Prevalence (%)': 0.1,
        'High Cholesterol Prevalence (%)': 0.05,
        'Teeth Lost Prevalence (%)': 0.05
    }

    standardized_data = data.copy()
    for column in weights.keys():
        mean = data[column].mean()
        std = data[column].std()
        standardized_data[column] = (mean - data[column]) / std

    weighted_data = standardized_data.copy()
    for column, weight in weights.items():
        weighted_data[column] *= weight

    weighted_data['Health Index'] = weighted_data[list(weights.keys())].sum(axis=1)

    data['Health Index'] = weighted_data['Health Index']

    new_path = 'data/cleaned/State_Health_Score.csv'
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    data.to_csv(new_path, index=False)