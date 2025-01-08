import os 
import pandas as pd
import requests
from config import *

def fetch_cdc_data(api_url, fields=None, batch_size=1000):
    """
    Fetch all data from the CDC API and return it as a pandas DataFrame.

    :param api_url: The API endpoint URL.
    :param fields: List of fields to fetch (optional).
    :param batch_size: Number of records to fetch per API call.
    :return: A pandas DataFrame containing the fetched data.
    """
    all_data = []
    offset = 0
    
    query_params = f"$limit={batch_size}&$offset={offset}"
    if fields:
        query_params = f"$select={','.join(fields)}&" + query_params
    
    while True:
        response = requests.get(f"{api_url}?{query_params}")
        if response.status_code != 200:
            raise Exception(f"API request failed: {response.status_code} - {response.text}")
        
        batch_data = response.json()
        if not batch_data:  # Stop if no more data
            break
        
        all_data.extend(batch_data)
        offset += batch_size
        query_params = query_params.replace(f"$offset={offset - batch_size}", f"$offset={offset}")
    os.makedirs(os.path.join("data", "raw"), exist_ok=True)
    pd.DataFrame(all_data).to_csv('data/raw/US_Counties_Health_Stats.csv', index=True, header=True)


def get_dataset():
    """_summary_
    Download the dataset and store it in data/raw directory
    """
    os.makedirs(os.path.join("data", "raw"), exist_ok=True)

    url = "https://data.cdc.gov/api/views/i46a-9kgh/rows.csv?accessType=DOWNLOAD"

    try:
        print("Downloading the dataset ...")

        response = requests.get(url)
        response.raise_for_status()

        output_path = os.path.join("data", "raw", "US_Counties_Health_Stats.csv")
        with open(output_path, 'wb') as f:
            f.write(response.content)

        print(f"Dataset saved to {output_path}")

    except Exception as e:
        print(f"Error : {e}")

    


