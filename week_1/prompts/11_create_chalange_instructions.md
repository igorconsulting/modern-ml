## Prompt

Create a notebook (`9_generate_full_training.ipynb`) that synthesizes all the steps from the week_1 notebooks to build a complete Kaggle notebook for submission to the competition. This notebook is intended to be used only on Kaggle.

Competition link: [Neo Bank Churn Prediction](https://www.kaggle.com/competitions/neo-bank-non-sub-churn-prediction/data)

1. Load all the Parquet raw data, including train and test datasets, and merge them. Refer to `week_1/notebooks/3_define_churn.ipynb` for guidance. Reduce memory usage by properly defining the types. The train data has the publicly available targets, and the test data only contains the features and will be used for submission to the leaderboard.
2. Perform feature engineering and define the target based on the days difference definition for the full load data (train + test) using the knowledge and code to build rolling window features from `week_1/notebooks/4_feature_engineering.ipynb`. Focus on the following features:
    - "interest_rate", "tenure", "prior_crypto_balance", "prior_mean_balance", "prior_sum_days_between", "prior_std_days_between", "prior_mean_days_between", "prior_max_days_between", "prior_mean_bank_transfer_in", "prior_mean_bank_transfer_out", "prior_mean_crypto_out", "prior_mean_bank_transfer_in_volume", "prior_mean_crypto_in_volume", "prior_sum_crypto_in_volume", "prior_sum_crypto_out_volume", "prior_10D_std_days_between", "prior_10D_mean_bank_transfer_out", "prior_90D_mean_days_between", "prior_90D_std_days_between", "prior_90D_min_days_between", "prior_90D_mean_bank_transfer_out", "prior_90D_mean_bank_transfer_in_volume", "prior_90D_mean_crypto_out_volume", "prior_180D_sum_days_between", "prior_180D_mean_days_between", "prior_180D_max_days_between", "prior_180D_min_days_between", "prior_180D_mean_balance", "prior_365D_sum_days_between", "prior_365D_mean_days_between", "prior_365D_std_days_between", "prior_365D_min_days_between", "prior_365D_mean_crypto_in_volume", "prior_450D_sum_days_between", "prior_450D_mean_days_between", "prior_450D_std_days_between", "prior_450D_max_days_between", "country", "broad_job_category"
3. Split the data into `train_df` (to perform training, tuning, and calibration) and `test_df` (to predict and save the prediction for submission to the competition).
4. Filter the train target according to the chosen target (420 days of inactivity). For example, if churn is defined as 420 days of inactivity, data older than 2022-10-01 cannot be used, with the last train data reference being 2023-12-31.
5. Tune the CatBoost model using all the training data with expanding window cross-validation to optimize (minimize) the log loss function. Refer to `week_1/notebooks/6_tuning.ipynb` for details. Use the same parameters for tuning as those in the referenced notebook.
6. Train a final CatBoost model with the tuned parameters using Venn Abers CVAP (Cross Venn Abers Calibration). Refer to `week_1/notebooks/6_tuning.ipynb` for an example:
    ```python
    va = VennAbersCalibrator(estimator=clf, inductive=False, n_splits=2)
    va.fit(X_train, y_train)
    va_cv_prob = va.predict_proba(X_test)
    ```
7. Save the prediction from the test dataset for submission to the leaderboard.
