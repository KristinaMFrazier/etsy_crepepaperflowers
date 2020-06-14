import requests
import json
import pandas as pd
import time

api_key = 'pcc1kj6mkrn2h59psstbf26s'

# attempt value isn't updating??

def get_data():
    attempt = 1
    while attempt <= 5:
        # Pull data from API
        r = requests.get('https://openapi.etsy.com/v2/listings/active?api_key={}&limit=100&offset={}'.format(api_key,((attempt-1)*100)))

        # Check success of API call
        print(r.status_code)

        # Convert JSON to dataframe to CSV output
        data = r.json()
        df = pd.DataFrame(data['results'])
        df.to_csv(path_or_buf='csv/etsylistings_20201106_{}.csv'.format(attempt))
        print("Attempt number {} succesful.".format(attempt))

        # Wait for 1 second
        time.sleep(1)

        # Pull the next 100 records
        attempt += 1

get_data()
