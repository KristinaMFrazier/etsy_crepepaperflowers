# load all data into a data frame
import numpy as np
import pandas as pd

full_dataset = "/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_etsy_listings_raw.csv"

converters = {"tags": lambda x: x.strip("[]").replace("'","").split(", "),"materials": lambda x: x.strip("[]").replace("'","").split(", ")}
data = pd.read_csv(full_dataset, converters = converters)

df = pd.DataFrame(data)

# Select relevant data columns

most_data = df[['listing_id','title','description','price','currency_code','quantity','views','num_favorers','when_made']]

# set the index as listing_id
set_index = most_data.set_index('listing_id')
most_data_export = pd.DataFrame(set_index)

# write data to a csv file
most_data_export.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_main_data_clean.csv")

# load tag data from csv into a dataframe
# use converters for read_csv to load columns as specific data types or objects
# tag_data = pd.read_csv(filepath_or_buffer = full_dataset,converters=tag_converter)

# select only listing_id and tag columns
tag_data_df = pd.DataFrame(data[['listing_id','tags']]).set_index('listing_id')

# explode tags and create a new dataframe
explode_tags = tag_data_df.explode('tags')
tag_data_exploded = pd.DataFrame(explode_tags)

# write tag data to a csv file
tag_data_exploded.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_tag_data_clean.csv")

# load materials data from csv into a dataframe
# materials_data = pd.read_csv(filepath_or_buffer = full_dataset,converters = {"materials": literal_eval})


# select only listing_id and materials columns
materials_data_df = pd.DataFrame(data[['listing_id','materials']]).set_index('listing_id')

# explode materials and create a new dataframe
explode_materials = materials_data_df.explode('materials')
materials_data_exploded = pd.DataFrame(explode_materials)

# write materials data to a csv file
materials_data_exploded.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_materials_data_clean.csv")
