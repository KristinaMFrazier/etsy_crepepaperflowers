# load all data into a data frame
import numpy as np
import pandas as pd

full_dataset = "/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_etsy_listings_raw.csv"

converters = {"tags": lambda x: x.strip("[]").replace("'","").split(", "),"materials": lambda x: x.strip("[]").replace("'","").split(", ")}
data = pd.read_csv(full_dataset, converters = converters)

df = pd.DataFrame(data)

#------------------------------------------------------------------------------
# MAIN DATA CSV
# Select relevant data columns

most_data = df[['listing_id','title','description','price','currency_code','quantity','views','num_favorers','when_made']]

# set the index as listing_id
set_index = most_data.set_index('listing_id')
most_data_export = pd.DataFrame(set_index)

# write data to a csv file
most_data_export.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_main_data_clean.csv")

#------------------------------------------------------------------------------
# TAG DATA CSV
# select only listing_id and tag columns
tag_data_df = pd.DataFrame(data[['listing_id','tags']]).set_index('listing_id')

# explode tags and create a new dataframe
explode_tags = tag_data_df.explode('tags')
tag_data_exploded = pd.DataFrame(explode_tags)

# write tag data to a csv file
tag_data_exploded.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_tag_data_clean.csv")

#------------------------------------------------------------------------------
# MATERIALS DATA CSV
# select only listing_id and materials columns
materials_data_df = pd.DataFrame(data[['listing_id','materials']]).set_index('listing_id')

# explode materials and create a new dataframe
explode_materials = materials_data_df.explode('materials')
materials_data_exploded = pd.DataFrame(explode_materials)

# write materials data to a csv file
materials_data_exploded.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_materials_data_clean.csv")

#------------------------------------------------------------------------------
# OCCASION DATA CSV
# select only listing_id and occasion columns
occasion_data_df = pd.DataFrame(data[['listing_id','occasion']]).set_index('listing_id')

# explode materials and create a new dataframe
explode_occasion = occasion_data_df.explode('occasion')
occasion_data_exploded = pd.DataFrame(explode_occasion)

# write materials data to a csv file
occasion_data_exploded.to_csv("/Users/kristinafrazier/documents/projects/etsy/data/csv_pf/all_occasion_data_clean.csv")
