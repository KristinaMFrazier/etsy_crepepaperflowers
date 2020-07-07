import requests
import json
import numpy as np
import pandas as pd
import time
from datetime import date

api_key = 'pcc1kj6mkrn2h59psstbf26s'

def get_data():
    attempt = 1
    while attempt <= 200:
        # Pull data from API
        r = requests.get('https://openapi.etsy.com/v2/listings/active?api_key={}&limit=100&offset={}&materials=”crepe paper”'.format(api_key,((attempt-1)*100)))

        # Check success of API call
        print(r.status_code)

        # Convert JSON to dataframe to CSV output
        data = r.json()
        today = date.today()
        df = pd.DataFrame(data['results'])
        df.to_csv(path_or_buf='csv_pf/etsylistings_{}_{}.csv'.format(today,attempt))
        print("Attempt number {} succesful.".format(attempt))

        # Wait for 1 second
        time.sleep(1)

        # Pull the next 100 records
        attempt += 1

get_data()
