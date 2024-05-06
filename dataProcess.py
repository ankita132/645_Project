import requests
import zipfile
import io
import pandas as pd

def download_and_extract_zip(url):
    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall('./')      
    else:
        print("Failed to download the zip file.")

def convert_data_to_csv(input_file, output_file):
    df = pd.read_csv(input_file, header=None)
    df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
                  'marital_status', 'occupation', 'relationship', 'race',
                  'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
                  'native_country', 'income']
    df.to_csv(output_file, index=False)

zip_url = "https://archive.ics.uci.edu/static/public/20/census+income.zip"
download_and_extract_zip(zip_url)
convert_data_to_csv('adult.data', 'adult.csv')
