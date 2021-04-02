# The ANZ Virtual Experience Repo

Data dictionary

1) status
- bool
- posted/ authorized
- Decription: posted means there are still transactions pending. Authorized is your available balance.
- 'posted' value is partically dependent on txn_descriptions of 'PAYMENT', 'INTER BANK', and 'PAY/SALARY'
- This makes sense since pending transactions are usually cash payments, bank transfers or corporate transactions

2) card_present_flag
- types of data: 1, 0, and NULL
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
