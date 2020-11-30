# Etsy Crepe Paper Flower Products Listing Analysis

## Project Purpose

The purpose of this project is to extract listings for crepe paper flower products from Etsy.com to maximize sales for the CrepeFloret shop. CrepeFloret is an Etsy shop that sells faux flower arrangements made of crepe paper. Insights uncovered from an analysis of listing data from competing shops may result in a competitive edge for CrepeFloret.

## Methodology

This set of Python and SQL code and Jupyter Notebooks includes a series of scripts to extract, compile, and clean a subset of Etsy listing data related to crepe paper flower products. Here is a concise summary of the project:
  - Creation of an interactive script to extract and compile listings from the Etsy API,
  - Data cleaning using Jupyter Notebooks,
  - Upload the data to PostgreSQL for long term storage, and completed an
  - Exploratory analysis of the data using Jupyter Notebooks, and
  - Creation of a final dashboard presenting the findings using Tableau Public.

Etsy listing data can only be extracted at a maximum of 100 records at a time. Python is used to compile the data into one dataset and to create additional tables, which all have a common listing_id column. SQL is used to explore the data. Details of the major steps involved in starting from pulling listing data from the Etsy API to ending the analysis with a set of SQL codes to answer questions about trends in the crepe paper flower market are as follows:

### Use Python to extract and combine, and clean Etsy listing data

The interactive python script for extracting and combining listing data is [here](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/master/datapullcombine_int.py):


### Store data in PostgreSQL

I created a database and schema to permanently store the csv datasets for future analysis, and uploaded each table to PostgreSQL through SQL Shell. Each SQL upload script is stored [in this file.](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/importdata_pf.sql)


### Conduct preliminary SQL analysis

A [series of SQL commands](https://github.com/KristinaMFrazier/etsy_crepepaperflowers/blob/pflistings/draftCPanalysis.sql) are used to answer questions related to understanding the crepe flower market on Etsy.


### Continue exploratory analysis in Python


### Present final analysis with Tableau Public
