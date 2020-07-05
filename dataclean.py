# load all data into a data frame
import numpy as np
import pandas as pd
from ast import literal_eval

data = pd.read_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv/all_etsy_listings_raw.csv")

df = pd.DataFrame(data)

# Select relevant data columns

most_data = df[['listing_id','title','description','price','currency_code','quantity','views','num_favorers','when_made']]

# set the index as listing_id
set_index = most_data.set_index('listing_id')
most_data_export = pd.DataFrame(set_index)

# write data to a csv file
most_data_export.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv/all_main_data_clean.csv")

# load tag data from csv into a dataframe
# use converters for read_csv to load columns as specific data types or objects
tag_data = pd.read_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv/all_etsy_listings_raw.csv",converters = {'tags':eval})

# select only listing_id and tag columns
tag_data_df = pd.DataFrame(tag_data[['listing_id','tags']]).set_index('listing_id')

# explode tags and create a new dataframe
explode_tags = tag_data_df.explode('tags')
tag_data_exploded = pd.DataFrame(explode_tags)

# write tag data to a csv file
tag_data_exploded.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv/all_tag_data_clean.csv")

# load materials data from csv into a dataframe
materials_data = pd.read_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv/all_etsy_listings_raw.csv",converters = {'materials':eval})


# select only listing_id and materials columns
materials_data_df = pd.DataFrame(materials_data[['listing_id','materials']]).set_index('listing_id')

# explode materials and create a new dataframe
explode_materials = materials_data_df.explode('materials')
materials_data_exploded = pd.DataFrame(explode_materials)

# write materials data to a csv file
materials_data_exploded.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv/all_materials_data_clean.csv")
