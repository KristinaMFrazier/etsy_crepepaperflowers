-- Helpful instructions: https://stackoverflow.com/questions/37432875/missing-data-for-column-while-trying-to-copy-a-csv-file-in-a-postgresql-database

-- IMPORT MAIN DATA TABLE
\copy july2020_2_active_listings (listing_id,title,description,price,currency_code,quantity,views,num_favorers,when_made) from '/Users/kristinafrazier/Documents/projects/etsy/data/csv_pf/all_main_data_clean.csv' delimiter ',' csv header;

-- IMPORT TAG DATA TABLE
\copy july2020_2_active_listings_tags (listing_id,tags) from '/Users/kristinafrazier/Documents/projects/etsy/data/csv_pf/all_tag_data_clean.csv' delimiter ',' csv header;

-- IMPORT MATERIALS DATA TABLE
\copy july2020_2_active_listings_materials (listing_id,materials) from '/Users/kristinafrazier/Documents/projects/etsy/data/csv_pf/all_materials_data_clean.csv' delimiter ',' csv header;

-- IMPORT OCCASION DATA TABLE
\copy july2020_2_active_listings_occasion (listing_id,occasion) from '/Users/kristinafrazier/Documents/projects/etsy/data/csv_pf/all_occasion_data_clean.csv' delimiter ',' csv header;

-- IMPORT DESCRIPTION WORDS DATA TABLE
\copy july2020_2_active_listings_descwords (listing_id,description) from '/Users/kristinafrazier/Documents/projects/etsy/data/csv_pf/all_descwords_data_clean.csv' delimiter ',' csv header;

-- IMPORT FLOWERLIST DATA TABLE
-- Source: https://www.alphalists.com/list/alphabetical-list-flowers
\copy july2020_flowerlist (flower) from '/Users/kristinafrazier/Documents/projects/etsy/data/csv_pf/flowerlist.csv' delimiter ',' csv header;
