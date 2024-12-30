PROMPT:

Please create a Python notebook at `./week_1/notebooks/3_feature_engineering.ipynb`. This notebook should:

1. Read the parquet file located at `./week_1/data/processed/full_churn_data_with_target.parquet`, using the column `Id` as the index.
2. Translate the provided DuckDB feature engineering query into equivalent pandas code, organizing the feature engineering steps into distinct code blocks.

Here is the DuckDB query for reference:

```sql
create or replace table base_model_data as
with churn_transaction as (
    select 
        customer_id,
        max(date) as date,
        1 as churner
    from train_data
    group by customer_id
    having max(date) < '2022-06-01')
, base_churn as (
    select 
        t.id,
        t.customer_id,
        t.country,
        t.date,
        t.tenure,
        coalesce(datediff(
            'day', 
            lag(t.date) over (partition by t.customer_id order by t.date), 
            t.date), 0) as days_between,
        datediff(
            'day', 
            t.date_of_birth, 
            t.date) / 365.25 as customer_age,
        case when t.from_competitor then 1 else 0 end as from_competitor,
        t.job,
        case when t.churn_due_to_fraud then 1 else 0 end as churn_due_to_fraud,
        log( 1 + t.atm_transfer_in) as atm_transfer_in,
        log( 1 + t.atm_transfer_out) as atm_transfer_out, 
        t.bank_transfer_in, 
        t.bank_transfer_out,
        t.crypto_in,
        t.crypto_out,
        t.bank_transfer_in_volume,
        t.bank_transfer_out_volume,
        t.crypto_in_volume,
        t.crypto_out_volume,
        t.interest_rate,
        coalesce(c.churner, 0) as churner,
        t.rowtype
    from 
        all_data t
        left join churn_transaction c 
            on c.customer_id = t.customer_id
            and c.date = t.date)
select 
    t.*,
    -- life time
    count(*)                       OVER previous as prior_count,
    mean(days_between)             OVER previous as prior_mean_days_between,
    max(days_between)              OVER previous as prior_max_days_between,
    mean(bank_transfer_in)         OVER previous as prior_mean_bank_transfer_in,
    mean(bank_transfer_out)        OVER previous as prior_mean_bank_transfer_out,
    mean(crypto_in)                OVER previous as prior_mean_crypto_in,
    mean(crypto_out)               OVER previous as prior_mean_crypto_out,
    mean(bank_transfer_in_volume)  OVER previous as prior_mean_bank_transfer_in_volume,
    mean(bank_transfer_out_volume) OVER previous as prior_mean_bank_transfer_out_volume,
    mean(crypto_in_volume)         OVER previous as prior_mean_crypto_in_volume,
    mean(crypto_out_volume)        OVER previous as prior_mean_crypto_out_volume,
    -- last 10 days
    count(*)                       OVER previous_10 as prior10_count,
    mean(days_between)             OVER previous_10 as prior10_mean_days_between,
    max(days_between)              OVER previous_10 as prior10_max_days_between,
    mean(bank_transfer_in)         OVER previous_10 as prior10_mean_bank_transfer_in,
    mean(bank_transfer_out)        OVER previous_10 as prior10_mean_bank_transfer_out,
    mean(crypto_in)                OVER previous_10 as prior10_mean_crypto_in,
    mean(crypto_out)               OVER previous_10 as prior10_mean_crypto_out,
    mean(bank_transfer_in_volume)  OVER previous_10 as prior10_mean_bank_transfer_in_volume,
    mean(bank_transfer_out_volume) OVER previous_10 as prior10_mean_bank_transfer_out_volume,
    mean(crypto_in_volume)         OVER previous_10 as prior10_mean_crypto_in_volume,
    mean(crypto_out_volume)        OVER previous_10 as prior10_mean_crypto_out_volume,
    -- last 450 days
    count(*)                       OVER previous_450 as prior450_count,
    mean(days_between)             OVER previous_450 as prior450_mean_days_between,
    max(days_between)              OVER previous_450 as prior450_max_days_between,
    mean(bank_transfer_in_volume)  OVER previous_450 as prior450_mean_bank_transfer_in_volume,
    mean(bank_transfer_out_volume) OVER previous_450 as prior450_mean_bank_transfer_out_volume,
    mean(crypto_in_volume)         OVER previous_450 as prior450_mean_crypto_in_volume,
    mean(crypto_out_volume)        OVER previous_450 as prior450_mean_crypto_out_volume,
    -- this month volume
    sum((bank_transfer_in_volume
        - bank_transfer_out_volume
        + crypto_in_volume
        - crypto_out_volume)) OVER this_week as this_week_volume,
    count(distinct customer_id) OVER this_week as this_week_customer_count
    
from 
    base_churn t
    WINDOW 
        -- whole lifetime so far
        previous AS (
            PARTITION BY customer_id 
            ORDER BY date 
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
        -- past 450 days
        previous_450 AS (
            PARTITION BY customer_id 
            ORDER BY date 
            RANGE BETWEEN INTERVAL 450 DAYS PRECEDING
                      AND INTERVAL  11 DAYS PRECEDING),
        -- past 10 days
        previous_10 AS (
            PARTITION BY customer_id 
            ORDER BY date 
            RANGE BETWEEN INTERVAL 10 DAYS PRECEDING
                      AND INTERVAL  1 DAYS PRECEDING),
        -- past 7 days country volume
        this_week AS (
            PARTITION BY country
            ORDER BY date
            RANGE BETWEEN INTERVAL 6 DAYS PRECEDING
                      AND CURRENT ROW)
```

The dataset has the following structure:

```plaintext
customer_id	interest_rate	name	country	date_of_birth	address	date	atm_transfer_in	atm_transfer_out	bank_transfer_in	...	tenure	from_competitor	job	churn_due_to_fraud	model_predicted_fraud	Usage	churn	next_date	days_diff	split
Id																					
1	1	3.5	Yolanda Parker	Lithuania	1954-07-10	1929 Erin Lights Suite 709\nLake Michaelburgh,...	2008-01-17	0	0	17476	...	0	False	Amenity horticulturist	False	False	NaN	0	2008-01-18	1.0	train
6	1	3.5	Yolanda Parker	Lithuania	1954-07-10	1929 Erin Lights Suite 709\nLake Michaelburgh,...	2008-01-18	0	0	19680	...	1	False	Amenity horticulturist	False	False	NaN	0	2008-01-19	1.0	train
16	1	3.5	Yolanda Parker	Lithuania	1954-07-10	1929 Erin Lights Suite 709\nLake Michaelburgh,...	2008-01-19	0	0	17958	...	2	False	Amenity horticulturist	False	False	NaN	0	2008-01-20	1.0	train
31	1	3.5	Yolanda Parker	Lithuania	1954-07-10	1929 Erin Lights Suite 709\nLake Michaelburgh,...	2008-01-20	0	0	22772	...	3	False	Amenity horticulturist	False	False	NaN	0	2008-01-21	1.0	train
Id																					
1	1	3.5	Yolanda Parker	Lithuania	1954-07-10	1929 Erin Lights Suite 709\nLake Michaelburgh,...	2008-01-17	0	0	17476	...	0	False	Amenity horticulturist	False	False	NaN	0	2008-01-18	1.0	train
6	1	3.5	Yolanda Parker	Lithuania	1954-07-10	1929 Erin Lights Suite 709\nLake Michaelburgh,...	2008-01-18	0	0	19680	...	1	False	Amenity horticulturist	False	False	NaN	0	2008-01-19	1.0	train
16	1	3.5	Yolanda Parker	Lithuania	1954-07-10	1929 Erin Lights Suite 709\nLake Michaelburgh,...	2008-01-19	0	0	17958	...	2	False	Amenity horticulturist	False	False	NaN	0	2008-01-20	1.0	train
31	1	3.5	Yolanda Parker	Lithuania	1954-07-10	1929 Erin Lights Suite 709\nLake Michaelburgh,...	2008-01-20	0	0	22772	...	3	False	Amenity horticulturist	False	False	NaN	0	2008-01-21	1.0	train
50	1	3.5	Yolanda Parker	Lithuania	1954-07-10	1929 Erin Lights Suite 709\nLake Michaelburgh,...	2008-01-21	0	0	23610	...	4	False	Amenity horticulturist	False	False	NaN	0	2008-01-23	2.0	train
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
7545935	165320	0.0	Mrs. Carol Foley	Romania	1994-12-19	2393 William Drive\nAlyssaton, MT 01733 Romania	2026-10-25	0	0	1874	...	0	False	Conservation officer, historic buildings	False	False	Private	0	NaT	NaN	test

Also has the following info():

<class 'pandas.core.frame.DataFrame'>
Index: 5286530 entries, 1 to 7545919
Data columns (total 30 columns):
 #   Column                    Dtype         
---  ------                    -----         
 0   customer_id               int64         
 1   interest_rate             float64       
 2   name                      object        
 3   country                   object        
 4   date_of_birth             object        
 5   address                   object        
 6   date                      datetime64[ns]
 7   atm_transfer_in           int64         
 8   atm_transfer_out          int64         
 9   bank_transfer_in          int64         
 10  bank_transfer_out         int64         
 11  crypto_in                 int64         
 12  crypto_out                int64         
 13  bank_transfer_in_volume   float64       
 14  bank_transfer_out_volume  float64       
 15  crypto_in_volume          float64       
 16  crypto_out_volume         float64       
 17  complaints                int64         
 18  touchpoints               object        
 19  csat_scores               object        
 20  tenure                    int64         
 21  from_competitor           bool          
 22  job                       object        
 23  churn_due_to_fraud        bool          
 24  model_predicted_fraud     bool          
 25  Usage                     object        
 26  churn                     int64         
 27  next_date                 datetime64[ns]
 28  days_diff                 float64       
 29  split                     object        
dtypes: bool(3), datetime64[ns](2), float64(6), int64(10), object(9)
memory usage: 1.1+ GB