# Etsy Crepe Paper Flower Products Market Analysis

## Project Purpose

The purpose of this project is to extract listings for crepe paper flower products from Etsy.com to maximize sales for the CrepeFloret shop. CrepeFloret is an Etsy shop that sells faux flower arrangements made of crepe paper. Insights uncovered from an analysis of listing data from competing shops may result in a competitive edge for CrepeFloret.

## Methodology

This set of Python and SQL code includes a series of scripts to extract, compile, and clean a subset of Etsy listing data related to crepe paper flower products. Etsy listing data can only be extracted at a maximum of 100 records at a time. Python is used to compile the data into one dataset and to create additional tables, which all have a common listing_id column. SQL is used to explore the data. Details of the major steps involved in starting from pulling listing data from the Etsy API to ending the analysis with a set of SQL codes to answer questions about trends in the crepe paper flower market are as follows:

### Use Python to extract, combine, and clean Etsy listing data

To extract, clean, and analyze Etsy listing data, the following file is executed: [datapullcombineclean.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/datapullcombineclean.py)

This master script executes the following scripts:
1. [datapull.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/datapull.py): Extracts csv files of listings with "crepe paper" listed as a material in 100-record increments.
2. [datacombine.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/datacombine.py): Combines all csv files of 100 records into one compiled csv.
3. [dataclean.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/dataclean.py): Creates a series of tables to upload to PostgreSQL data model.
4. [dataclean_desctext.py](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/dataclean_desctext.py): Additional table creation of each word used in the description of a listing.

### Design PostgreSQL data model

A database and schema was designed and deployed to store csv outputs for SQL analysis. The analysis requires one data table where each row corresponds to one listing and includes several columns of attribute data for each listing, which is created by dataclean.py. Additionally, both dataclean.py and dataclean_desctext.py create additional data tables for each tag, material, of description word per listing_id. All tables can be joined for analysis using the common listing_id field.

### Upload CSV files to PostgreSQL schema

The csv outputs of these scripts, as well as an additional csv of a list of flowers, are then uploaded to PostgreSQL through SQL Shell. Each SQL upload script is stored [in this file.](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/importdata_pf.sql)

### Use SQL commands to extract insights

A [series of SQL commands](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/draftCPanalysis.sql) are used to answer questions related to understanding the crepe flower market on Etsy.

## Insights

The SQL commands used to analyze the Etsy listing data resulted in the following valuable insights and findings that may help improve sales of CrepeFloret products:
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

## Continuous Improvement

The scripts outlined in the Methdology above were first committed to GitHub in July 2020. The author of these scripts is interested to make the following improvements in future updates:
* Refactor Python extract/combine/clean codes to take user input for how many files to export and directory paths for CSV outputs
* Improve documentation for python scripts
* Create unique ids to replace listing id column (some listing ids are repeated, so this collumn cannot be used as a primary key in PostgreSQL).
* Add and refine SQL commands to uncover additional insights
