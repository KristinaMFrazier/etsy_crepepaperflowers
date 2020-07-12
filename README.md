# Etsy Crepe Paper Flower Products Market Analysis
### *Market analysis of crepe paper flower products to maximize sales for the CrepeFloret shop*

**PROJECT PURPOSE**
The purpose of this project is to extract listings for crepe paper flower products from Etsy.com to maximize sales for the CrepeFloret shop.

**METHODOLOGY**
This set of Python and SQL code includes a series of scripts to extract, compile, and clean a subset of Etsy listing data related to crepe paper flower products. Etsy listing data can only be extracted at a maximum of 100 records at a time. Python is needed to compile the data into one dataset, and to create additional tables related by each listing's listing_id column.

*Use Python to extract, combine, and clean Etsy listing data*

To extract, clean, and analyze Etsy listing data, the following file is executed: [datapullcombineclean.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/datapullcombineclean.py)

This master script executes the following scripts:
1. [datapull.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/datapull.py): Extracts csv files of listings with "crepe paper" listed as a material in 100-record increments.
2. [datacombine.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/datacombine.py): Combines all csv files of 100 records into one compiled file.
3. [dataclean.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/dataclean.py): Creates a series of tables to upload to PostgreSQL data model.
4. [dataclean_desctext.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/dataclean_desctext.py): Additional table creation of each word used in the description of a listing.

*Design PostgreSQL data table model*
A database and schema was designed and deployed to store CSV outputs for SQL analysis. The analysis requires one data table where each row corresponds to one listing and includes several columns of attribute data for each listings, which is created by dataclean.py. Additionally, both dataclean.py and dataclean_desctext.py create additional data tables for each tag, material, of description word per listing id. All tables can be joined for analysis using a common listing_id field.

*Upload CSV files to PostgreSQL schema*
The csv outputs of these scripts, as well as an additional CSV of a list of flowers, are then uploaded to PostgreSQL through SQL Shell. Each SQL upload script is stored [in this file.](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/importdata_pf.sql)

*Use SQL commands to extract insights*
A [series of SQL commands](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/draftCPanalysis.sql) are used to answer questions related to understanding the crepe flower market on Etsy.

**INSIGHTS**
The SQL commands used to analyze the Etsy listing data resulted in the following helpful insights and findings that may help improve sales of CrepeFloret products:
* The average price of a crepe paper flower bouquet sold in USD is approximately $58.
* The top five most popular tags for crepe paper flower products are, in order of popularity:
  * paper flowers
  * crepe paper flowers
  * mexican flowers
  * day of the dead
  * Cinco De Mayo
* The most popular occasions are, in order of popularity, day of the dead, weddings, cinco de mayo, and St. Patricks day. It is important to note that the occasion field is not commonly populated for listings.
* The top five most popular flowers for crepe paper flower products are, in order of popularity:
  * rose
  * peony
  * ranunculus
  * lavender
  * hydrangea
* It is more common to find made-to-order products than pre-made products.

**CONTINUOUS IMPROVEMENTS**
The scripts outlined in the Methdology above were first committed to GitHub in July 2020. The author of these scripts is interested to make the following improvements in future updates:
* Refactor python extract/combine/clean codes to take user input for how many files to export and directory paths for CSV outputs
* Improve documentation for python scripts
* Create unique ids
* Add and refine SQL commands for robust Etsy listing analysis
