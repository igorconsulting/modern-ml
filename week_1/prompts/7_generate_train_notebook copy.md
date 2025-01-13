## Prompt

### Global Variables
- `train_max_date = 2023-01-01`
- `validation_max_date = 2024-01-01`
- `features = ["interest_rate", "country", "atm_transfer_in", "atm_transfer_out", "bank_transfer_in", "bank_transfer_out", "crypto_in", "crypto_out", "bank_transfer_in_volume", "bank_transfer_out_volume", "crypto_in_volume", "crypto_out_volume", "complaints", "tenure", "from_competitor", "job", "churn_due_to_fraud", "model_predicted_fraud", "appointment", "email", "phone", "whatsapp", "days_between", "customer_age", "prior_emails", "prior_appointments", "prior_phones", "prior_whatsapps", "prior_count", "prior_bank_balance", "prior_crypto_balance", "prior_mean_days_between", "prior_min_days_between", "prior_max_days_between", "prior_mean_bank_transfer_in", "prior_mean_bank_transfer_out", "prior_mean_crypto_in", "prior_mean_crypto_out", "prior_mean_bank_transfer_in_volume", "prior_mean_bank_transfer_out_volume", "prior_mean_crypto_in_volume", "prior_mean_crypto_out_volume", "prior_10D_count", "prior_10D_mean_days_between", "prior_10D_max_days_between", "prior_10D_min_days_between", "prior_10D_mean_bank_transfer_in", "prior_10D_mean_bank_transfer_out", "prior_10D_mean_crypto_in", "prior_10D_mean_crypto_out", "prior_10D_mean_bank_transfer_in_volume", "prior_10D_mean_bank_transfer_out_volume", "prior_10D_mean_crypto_in_volume", "prior_10D_mean_crypto_out_volume", "prior_90D_count", "prior_90D_mean_days_between", "prior_90D_max_days_between", "prior_90D_min_days_between", "prior_90D_mean_bank_transfer_in", "prior_90D_mean_bank_transfer_out", "prior_90D_mean_crypto_in", "prior_90D_mean_crypto_out", "prior_90D_mean_bank_transfer_in_volume", "prior_90D_mean_bank_transfer_out_volume", "prior_90D_mean_crypto_in_volume", "prior_90D_mean_crypto_out_volume", "prior_180D_count", "prior_180D_mean_days_between", "prior_180D_max_days_between", "prior_180D_min_days_between", "prior_180D_mean_bank_transfer_in", "prior_180D_mean_bank_transfer_out", "prior_180D_mean_crypto_in", "prior_180D_mean_crypto_out", "prior_180D_mean_bank_transfer_in_volume", "prior_180D_mean_bank_transfer_out_volume", "prior_180D_mean_crypto_in_volume", "prior_180D_mean_crypto_out_volume", "prior_365D_count", "prior_365D_mean_days_between", "prior_365D_max_days_between", "prior_365D_min_days_between", "prior_365D_mean_bank_transfer_in", "prior_365D_mean_bank_transfer_out", "prior_365D_mean_crypto_in", "prior_365D_mean_crypto_out", "prior_365D_mean_bank_transfer_in_volume", "prior_365D_mean_bank_transfer_out_volume", "prior_365D_mean_crypto_in_volume", "prior_365D_mean_crypto_out_volume", "prior_450D_count", "prior_450D_mean_days_between", "prior_450D_max_days_between", "prior_450D_min_days_between", "prior_450D_mean_bank_transfer_in", "prior_450D_mean_bank_transfer_out", "prior_450D_mean_crypto_in", "prior_450D_mean_crypto_out", "prior_450D_mean_bank_transfer_in_volume", "prior_450D_mean_bank_transfer_out_volume", "prior_450D_mean_crypto_in_volume", "prior_450D_mean_crypto_out_volume", "this_week_bank_volume", "this_week_crypto_volume"]`
- `target = 'churn'`

### About the Dataset
* It is a Machine Learning classification problem.
* The target variable is the 'churn' column.
* Here is the columns info() of the dataset:

### Task
Create a Python notebook at `./week_1/notebooks/5_train_the_model.ipynb` that performs the following tasks:

1. **Read Data:**
    - Read the parquet file `./week_1/data/processed/feature_engineering_dataset.parquet`.

2. **Preprocessing:**
    - Cast categorical features to the type category, fill NaNs with an empty string.
    - Create the cat_features list based on the columns types (objects)

3. **Train, Validation, Test Split:** 
    - Create a list with the features that will be used by the model (exclude the target column `churn`)
    - Create the target string variable with the value `churn`
    
    - Create train dataset (train_df) where `date` is < `train_max_date`.
    - Create validation datasets (validation_df) where `date` is >= `train_max_date` and < `validation_max_date`.
    - Create a test dataset (test_df) where `date` > `validation_max_date`.

4. **Train a Vanilla Baseline CatBoost Model:**
    - Train a vanilla CatBoost model.
    - Compute the main metrics of the baseline: Log loss, precision-recall AUC (average precision), ROC AUC, Brier score.
    - Plot the precision-recall curve and the calibration curve.

5. **Feature Selection with Boruta:**
    - Use a vanilla CatBoost model to select the main features using the Leshy algorithm from the ARFS library (https://arfs.readthedocs.io/en/latest/notebooks/arfs_classification.html):
    - Example code of ARFS
     -  '''model = CatBoostClassifier(random_state=42, verbose=0)

        feat_selector = arfsgroot.Leshy(
            model, n_estimators=20, verbose=1, max_iter=50, random_state=42, importance="permutation"
        )          

        feat_selector.fit(X=X_train, y=y_train)

        selector = feat_selector
        selected_features = feat_selector.get_feature_names_out()'''
    - Get selected features inside a feature selection list
    - Plot the Leshy importance plot.
    - Create a list of cat_features after feature selection

6. **Train a Vanilla CatBoost Model with Selected Features:**
    - Train a vanilla CatBoost model with the selected features.
    - Compute the main metrics of the baseline: Log loss, precision-recall AUC (average precision), ROC AUC, Brier score.
    - Plot the precision-recall curve and the calibration curve.

7. **Perform Optuna Hyperparameter Tuning:**
    - Use Optuna to find the best hyperparameters.
    - Search over the most important CatBoost parameters.
    - Optimize for Log Loss.
    - Retrain the model with the best parameters.

8. **Perform Model Calibration:**
    - Apply model calibration using the sklearn sigmoid function.
    - Recompute the main metrics of the baseline: Log loss, precision-recall AUC (average precision), ROC AUC, Brier score.
    - Plot the precision-recall curve and the calibration curve.

9.  **Plot SHAP and Permutation Importance:**
    - Plot the final SHAP summary plot.
    - Plot the Permutation importance plot.
