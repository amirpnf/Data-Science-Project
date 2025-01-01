import os 
import pandas as pd
import requests

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

if __name__ == "__main__":
    get_dataset()

    


