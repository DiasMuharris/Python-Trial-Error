import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.lazada.co.id/botol-minum/?rating=4'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data into a list or DataFrame
    data_list = []

    # Example: Extracting titles from <h2> tags
    titles = soup.find_all('h2')
    for title in titles:
        data_list.append(title.text)

    # Create a DataFrame
    df = pd.DataFrame(data_list, columns=['Titles'])

    # Save to Excel with xlsx extension using openpyxl engine
    df.to_excel('output_data.xlsx', index=False, engine='openpyxl')

print(df)
