---
Version: 1.0
Author: Isaac Kar Wai Low
Title: ANZ Virtual Internship Project: Data@ANZ
Link: https://www.theforage.com/virtual-internships/prototype/ZLJCsrpkHo9pZBJNY/Data%40ANZ%20Program
DateTimeCreated: 03/04/2021 2:44 AM
---
## Summary

As part of the virtual internship for Data @ANZ, I have used the synthesized transaction dataset that contains 3 months' worth of transactions for 100 hypothetical customers. It contains purchases, recurring transactions, and salary transactions.

The dataset is designed to simulate realistic transaction behaviours that are observed in ANZ's real transaction data, so many of the insights to be gathered from the tasks will be genuine.

## Assumptions and Limitations

* The dataset only shows 3 month's worth of data in 2018, and so cannot be used to predict trends or insights post 2018 unless advised otherwise.

* Meanings of field column headers are inferred from how transactions generally work. A data dictionary was created as a 'single source of truth' for interpreting the data.

* The data dictionary is made as a reference for the ideal field details of the dataset. This means that the dictionary may contain added or deleted fields that were not part of the original dataset. All data type conversions should reflect the minimal prescriptions as laid out in the data dictionary.

* All added fields to the original dataset has been inferred from the original data.

* Many of the additional fields that are either included or excluded from the original synthesized transaction dataset on load has already been dealt with in Excel. These preliminary procedures are dealt with in passing at the start of this notebook.

## Technology Used

* Jupyter notebooks
* Anaconda
* Python 3.8.5
* Pandas
* Datetime

## Data dictionary

| Field Name        | Legal Values                                                   | Data Type | Field Size |
|-------------------|----------------------------------------------------------------|-----------|------------|
| timestamp         | '%Y-%m-%d %H:%M:%S'                                            | datetime  | 64         |
| date              | '%m-%d-%Y'                                                     | date      | 64         |
| status            | authorized/ posted                                             | category  |            |
| card_present_bool | True, False                                                    | bool      | 32         |
| card_present_cat  | 1, 0                                                           | category  |            |
| age               | years                                                          | int       | 32         |
| gender            | M, F                                                           | category  |            |
| txn_description   | POS, SALES-POS, PAYMENT, INTER<br>BANK, PAY/SALARY, PHONE BANK | category  |            |
| balance           | numeric                                                        | float     | 64         |
| amount            | numeric                                                        | float     | 64         |
| geometry          | any                                                            | object    |            |
| long              | range: -180, 180                                               | float     | 64         |
| lat               | range: -90, 90                                                 | float     | 64         |
| merch_suburb      | any                                                            | object    |            |
| merch_state       | any                                                            | object    |            |
| merch_geometry    | any                                                            | object    |            |
| merch_long        | range: -180, 180                                               | float     | 64         |
| merch_lat         | range: -90, 90                                                 | float     | 64         |

## Preliminary Data Preperation

3. Gather some interesting overall insights about the data. For example -- what is the average transaction amount? How many transactions do customers make each month, on average? 

Segment the dataset by transaction date and time. Visualise transaction volume and spending over the course of an average day or week. Consider the effect of any outliers that may distort your analysis.

5. For a challenge – what insights can you draw from the location information provided in the dataset?

6. Put together 2-3 slides summarising your most interesting findings to ANZ management.
