## Prompt

### Global Variables
- `exiceded_max_inactivity = 365`

### Task
Create a Python notebook at `./week_1/notebooks/2_define_churn.ipynb` that performs the following tasks:

1. **Read Data:**
    - Read all parquet files matching the pattern `./week_1/data/raw/train_*.parquet`.

2. **Define Churn Variable:**
    - Add a placeholder column with churn value set to 0.
    - Sort values by `customer_id` and by `date`
    - Group users by `customer_id`.
    - Calculate the difference in days between customer transaction dates. For the last date column, calculate the difference with the `max_dataset_date` (the cutoff date).
    - Mark churn as 1 (true) if the difference between a customer transaction exiceded  `exiceded_max_inactivity` days.

### Context
You have been hired as a data scientist at a bank facing significant competition and potential customer churn. Initial experiments suggest that customer behavior can be predicted, but a formal churn definition does not exist. Your goal is to create a churn definition, implement it, and predict churn.

### Data Description
The parquet data includes the following columns:
- `Id`: Unique ID of the daily table
- `customer_id`: Unique customer ID
- `interest_rate`: Bank account interest rate on that day
- `name`: Name of the person
- `country`: Country of the person
- `date_of_birth`: Date of birth of the person
- `address`: Current address of the person
- `date`: Date of the events
- `atm_transfer_in`: Number of ATM pay-ins
- `atm_transfer_out`: Number of ATM withdrawals
- `bank_transfer_in`: Number of in-going transactions
- `bank_transfer_out`: Number of out-going transactions
- `crypto_in`: Number of buying-crypto transactions
- `crypto_out`: Number of selling-crypto transactions
- `bank_transfer_in_volume`: Total volume of in-going transactions
- `bank_transfer_out_volume`: Total volume of out-going transactions
- `crypto_in_volume`: Total volume of buying-crypto transactions
- `crypto_out_volume`: Total volume of selling-crypto transactions
- `churn`: Flag indicating if the customer will not perform any action in the next 12 months (TARGET COLUMN)
- `complaints`: Number of complaints made
- `touchpoints`: List of support touchpoints the customer had that day (contains the channel name the customer reached out via)
- `csat_scores`: Customer satisfaction score based on the support touchpoint (nested dictionary with CSAT by support channel)
- `tenure`: Days since the customer signed a contract with the bank or had product activity for the first time
- `from_competitor`: Flag indicating if the customer came from a competitor
- `job`: Customer's job title

Keep all text and code in English.
