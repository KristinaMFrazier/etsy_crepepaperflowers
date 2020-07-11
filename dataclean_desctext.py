# load all data into a data frame
import numpy as np
import pandas as pd

full_dataset = "/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_etsy_listings_raw.csv"

converters = {"description": lambda x: x.strip("[]").replace("-"," ").replace(":"," ").replace(";"," ").replace("("," ").replace(")"," ").replace("#"," ").replace("'","").replace(",","").replace("$","").replace("!","").replace("&","").replace(".","").split(" ")}

data = pd.read_csv(full_dataset, converters = converters)

df = pd.DataFrame(data)

#------------------------------------------------------------------------------
# DESCRIPTION WORDS
# Select relevant data columns
desc_words = pd.DataFrame(data[['listing_id','description']]).set_index('listing_id')

# explode materials and create a new dataframe
explode_descwords = desc_words.explode('description')
desc_words_exploded = pd.DataFrame(explode_descwords)

# write materials data to a csv file
desc_words_exploded.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_descwords_data_clean.csv")
