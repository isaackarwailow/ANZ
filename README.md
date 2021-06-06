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

| Field Name        | Key / description   | Data Type |
|-------------------|---------------------|-----------|
| timestamp         | '%Y-%m-%d %H:%M:%S' | datetime  |
| date              | '%m/%d/%Y'          | datetime  |
| status            | authorized/ posted  | category  |
| card_present_flag | 1, 0                | category  |
| account           | sequence of numbers | object    |
| first_name        | string              | object    |
| age               | years               | int       |
| gender            | M, F                | category  |
| txn_description   | type of transaction | category  |
| balance           | numeric             | float     |
| amount            | numeric             | float     |
| geometry          | any                 | object    |
| X                 | range: -90, 90      | float     |
| Y                 | range: -180, 180    | float     |
| merch_suburb      | any                 | object    |
| merch_state       | any                 | object    |
| merch_geometry    | any                 | object    |
| merch_X           | range: -90, 90      | float     |
| merch_Y           | range: -180, 180    | float     |
| distance          | kilometers          | float     |
| country           | string              | object    |

## Preliminary Data Preperation using MS Excel

It is important to note that the csv file loaded into the pandas library as a DataFrame object has already had some non-trivial data cleaning performed on it in Excel. The following outlines the detailed steps taken to get the original ANZ synthesized transactions dataset to match the ideal data dictionary that I have created for further data wrangling with Python.

1. The `extraction` column can be used for time-indexing since it has a `pandas.DatetimeIndex` compatible format. Change the column heading from 'extraction' to 'timestamp' and `shift + drag` the column to index 0 or A1 in Excel. This would satisfy 1NF rules.

2. Next, delete `bpay_biller_code, currency, merchant_id, merchant_code, first_name, date, transaction_id, country, customer_id, movement`. The reasoning behind these decisions are outlined briefly here:

    * `date, transaction_id, merchant_id`: Column fields violate 2NF as the column is functionally dependent on the primary key. Since I want to parse timestamps as the index of my DataFrame these columns must be deleted
    * `currency, country`: Column fields are transitively dependent and contain non-unique rows. Therefore, 3NF is violated
    * `account, customer_id, first_name`: These are transitively dependent and not very useful for our time-series analysis. Note that there are other transitive dependencies as well, such as `gender` and `age`. However since we are not designing a relational database in this analysis, those columns are still kept just in case
    * `bpay_biller_code, merchant_code, and movement` are transitively dependent and so are removed as they violate 3NF
    * *Note:* Even though column deletion follows normalization guidelines, this *does not* mean that the schema of this table follows normalization rules, as it clearly does not. Normalization rules were only used as a guideline for preliminary data cleaning. Therefore, it is recommended to use the original dataset instead if a person wishes to create a relational schema instead.

3. Create columns `X, Y, merch_X`, and `merch_Y`: these olumns are extracted from `long_lat` and `merch_long_lat` so that they can be easily plotted on a `folium.Map` object. Use the Excel formula with form:

   ```Excel
   +N(formulas for X = lat, Y = long, merch_X = merch_lat, merch_Y = merch_long)
   = IF(LEN(Y)<>0,LEFT(Y,FIND(" ",Y)-1),0)
   = IF(LEN(X)<>0, RIGHT(X, (LEN(X))-(FIND(" ",X))), 0)
   +N(for merch_X and merch_Y, substitute the values into above formulas)
   ```

4. Calculate the distance between the corrdinates and save it into the field `coord_diff_km` with this formula, substituting the appropriate values:

   ```Excel
   = IF(merch_X=0,0,(3443.8985*1.852001*(ACOS((SIN(X*PI()/180)*SIN(merch_X*PI()/180)+COS(X*PI()/180)*COS(merch_X*PI()/180)*COS(merch_Y*PI()/180-Y*PI()/180))))))
   ```

## Task 2 Questions

* For this task, you’ll likely need to use statistical software such as R, SAS, or Python.

* Using the same transaction dataset, identify the annual salary for each customer

* Explore correlations between annual salary and various customer attributes (e.g. age). These attributes could be those that are readily available in the data (e.g. age) or those that you construct or derive yourself (e.g. those relating to purchasing behaviour). Visualise any interesting correlations using a scatter plot.

* Build a simple regression model to predict the annual salary for each customer using the attributes you identified above

* How accurate is your model? Should ANZ use it to segment customers (for whom it does not have this data) into income brackets for reporting purposes?

* For a challenge: build a decision-tree based model to predict salary. Does it perform better? How would you accurately test the performance of this model?

## Appendix

### Models and training times

| Model         | CV Search Flag | CV Search Type | Wall Time  |
|---------------|----------------|----------------|------------|
| Decision Tree | Yes            | Grid           | 1min 27s |
| Random Forest | Yes            | Grid           | 4min 34s |

### References

* For feature engineering X and Y coordinates: <https://bmanikan.medium.com/feature-engineering-all-i-learned-about-geo-spatial-features-649871d16796>
* For tuning hyperparameters for Random Forest: https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74
* 