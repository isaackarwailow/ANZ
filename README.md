---
Version: 1.0
Author: Isaac Kar Wai Low
Title: Virtual Internship - Data@ANZ
Link: https://www.theforage.com/virtual-internships/prototype/ZLJCsrpkHo9pZBJNY/Data%40ANZ%20Program
DateTimeCreated: 03/04/2021 2:44 AM
---
# ANZ Virtual Internship Project: Data@ANZ
## Technology Used
* Jupyter notebooks
* Anaconda
* Python 3.8.5

## Data dictionary

| Field Name        | Legal Values                                              | Data Type | Field Size |
|-------------------|-----------------------------------------------------------|-----------|------------|
| timestamp         | '%Y-%m-%d %H:%M:%S'                                       | datetime  | 64         |
| date              | '%m-%d-%Y                                                 | date      | 64         |
| status            | authorized/ posted                                        | category  |            |
| card_present_bool | True, False                                               | bool      | 32         |
| card_present_cat  | 1, 0                                                      | category  |            |
| age               | years                                                     | int       | 32         |
| gender            | M, F                                                      | category  |            |
| txn_description   | POS,SALES-POS,PAYMENT,INTER<br>BANK,PAY,SALARY,PHONE BANK | category  |            |
| balance           | numeric                                                   | float     | 64         |
| amount            | numeric                                                   | float     | 64         |
| geometry          | string                                                    | object    |            |
| long              | range: -180, 180                                          | float     | 64         |
| lat               | range: -90, 90                                            | float     | 64         |
| merch_suburb      | string                                                    | object    |            |
| merch_state       | string                                                    | object    |            |
| merch_geometry    | string                                                    | object    |            |
| merch_long        | range: -180, 180                                          | float     | 64         |
| merch_lat         | range: -90, 90                                            | float     | 64         |

## Guide
1. Load the transaction dataset below into an analysis tool of your choice (Excel, R, SAS, Tableau, or similar)
- I chose Jupyter Notebooks and Python 3.8.5, loading the dataset as a csv file into the notebook via pandas library read_csv method.
2. Start by doing some basic checks – are there any data issues? Does the data need to be cleaned?
- I made a data dictionary in order to make the values to be easily indexed. For example, card_present can be thought of as a Boolean value so a new column was made using 1 and 0 as a guide.
    -   **Data types**
        - *timestamp*: timestamp is fornmatted to the precision of seconds so a datetime64 would suffice
        - 
    - **Missing Values**
        - *card_present*: empty values are equivalent to a False status, so missing values are replaced with bools
- 
3. Gather some interesting overall insights about the data. For example -- what is the average transaction amount? How many transactions do customers make each month, on average?
4. Segment the dataset by transaction date and time. Visualise transaction volume and spending over the course of an average day or week. Consider the effect of any outliers that may distort your analysis.
5. For a challenge – what insights can you draw from the location information provided in the dataset?
6. Put together 2-3 slides summarising your most interesting findings to ANZ management.

1) status
- bool
- posted/ authorized
- Decription: posted means there are still transactions pending. Authorized is your available balance.
- 'posted' value is partically dependent on txn_descriptions of 'PAYMENT', 'INTER BANK', and 'PAY/SALARY'
- This makes sense since pending transactions are usually cash payments, bank transfers or corporate transactions

2) card_present_flag
- types of data: 1, 0
- Note: The null value violates 2NF (2nd Normal Form) due to it being a non-prime attribute being functionally dependent on status. If this value is normalized, it will also make status bool redundant

3) bpay_biller_code
- does not give us any useful information other than 0 and NULL
- Value 0 has functional dependencies on status 'posted' and 'PAY/SALARY' under txn_description

4) Account
- only potential candidate key for indexing the record
- exclude 'ACC' from record for better querying and index retrieval

5) Currency
- redundant data as there are no distinct values in the series

6) long_lat
- the geolocation of the transaction
- can use a map API to get the value that ATMS still bring to a hot/ cold area

7) txn_description
- INTER BANK: bank transfer
- PAY/SALARY: corporate transaction
- PAYMENT: internet payment/ other
- PHONE BANK: Paid by phone
- POS: Point of Sale - Credit purchase
- SALES-POS: - Credit sale

8) merchant_id
- NULL values funtionally dependent on 'posted'

9) merchant_code
- functionally dependent on bpay_biller_code
- can delete due to redundancy

10) first_name
- non_prime string value

11) balance
- float type currency indicator

12) date
- day/Year value is not unique
- Can be sorted by month with fairly equal distributions

13) gender
- string 'F' or 'M'

14) age
- int

15) extraction
- time can be extracted to make forecasts on daily usages throughout the day
- date is not very useful as it is repeated in date column

16) amount
- float type
- can be contrasted to balance to forecast purchasing behaviour
- can be used to make a budget planning app in ANZ mobile phone

17) customer_id
- another candidate key like account number

18) movement
- all 'credit' has something to do with 'PAY/SALARY'/ corporate transactions which is probably why the biller_code and merchant_codes were all 0 because data entry person knew that these were non-traditional transactions.
- these can be taken out from the analyses unless a specific use case is needed to make analyses between debit and credit, which is unlikely

What to with dataset?
Assumptions:
From the recent annual report of 2020 from ANZ, the top priorities for the bank are
1) Environmental,Social, and Governance (ESG) Reporting: this includes the potential to launch better campaigns for promoting safe spending habits in poorly educated areas, for example.
2) ANZ's reponse to COVID-19 in supporting customers, employees and the community.

Statement of purpose:
This dataset starts with the hypothesis that ANZ can cut costs by understanding which areas still require brick and mortar branches, by understanding the correlation of frequency of transactions and the amount of COVID-19 cases by plotting it against a geolocation on the map as the control variable
