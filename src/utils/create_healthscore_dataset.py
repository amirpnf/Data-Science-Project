import pandas as pd
import os
from config import *

def create_health_score():

    data = pd.read_csv(CLEANED_DATA_DIR)

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

    weighted_data['Health Score'] = weighted_data[list(weights.keys())].sum(axis=1)

    data['Health Score'] = weighted_data['Health Score']

    new_path = HEALTH_SCORE
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    data.to_csv(new_path, index=False)

def create_health_score_by_state():
    data = pd.read_csv(STATE_DATA_DIR)

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

    weighted_data['Health Score'] = weighted_data[list(weights.keys())].sum(axis=1)

    data['Health Score'] = weighted_data['Health Score']

    new_path = STATE_HEALTH_SCORE
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    data.to_csv(new_path, index=False)