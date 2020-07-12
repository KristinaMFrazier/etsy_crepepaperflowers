# Etsy Crepe Paper Flower Products Market Analysis
### *Market analysis of crepe paper flower products to maximize sales for the CrepeFloret shop*

**Project Purpose**
The purpose of this project is to extract listings for crepe paper flower products from Etsy.com to maximize sales for the CrepeFloret shop.

**Methodology**
This set of Python and SQL code includes a series of scripts to extract, compile, and clean a subset of Etsy listing data related to crepe paper flower products. Etsy listing data can only be extracted at a maximum of 100 records at a time. Python is needed to compile the data into one dataset, and to create additional tables related by each listing's listing_id column.

To extract, clean, and analyze Etsy listing data, the following file is executed: [datapullcombineclean.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/datapullcombineclean.py)

This master script executes the following scripts:
1. [datapull.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/datapull.py): Extracts csv files of listings with "crepe paper" listed as a material in 100-record increments.
2. [datacombine.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/datacombine.py): Combines all csv files of 100 records into one compiled file.
3. [dataclean.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/dataclean.py): Creates a series of tables to upload to PostgreSQL data model.
4. [dataclean_desctext.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/dataclean_desctext.py): Additional table creation of each word used in the description of a listing.

The csv outputs of these scripts are then uploaded to PostgreSQL through SQL Shell. Each SQL upload script is stored in this file.

And a series of SQL commands are used to answer questions related to understanding the crepe flower market on Etsy.

**Insights**

**Continuous Improvements**
The scripts outlined in the Methdology above were first commited to GitHub in July 2020
