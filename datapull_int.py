import requests
import json
import numpy as np
import pandas as pd
import time
from datetime import date

print("Hello! Where do you want to store the data?: ")
folder = input()

print("Great! And how many pages of listings? (Every page has 100 listings): ")
listing_num = input()
listing_num = int(listing_num)

key = open('apikey.txt', 'r')

api_key = key.read()

key.close()

def get_data():
    attempt = 1
    while attempt <= listing_num:
        # Pull data from API
        r = requests.get('https://openapi.etsy.com/v2/listings/active?api_key={}&limit=100&offset={}&materials=”crepe paper”'.format(api_key,((attempt-1)*100)))

        # Check success of API call
        print(r.status_code)

        # Convert JSON to dataframe to CSV output
        data = r.json()
        today = date.today()
        df = pd.DataFrame(data['results'])
        df.to_csv(path_or_buf='{}/etsylistings_{}_{}.csv'.format(folder,today,attempt))
        print("Attempt number {} succesful.".format(attempt))

        # Wait for 1 second
        time.sleep(1)

        # Pull the next 100 records
        attempt += 1

get_data()
