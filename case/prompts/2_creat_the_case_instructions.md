## PROMPT
Create instructions for the final project case of this course repository. wiht the following content :

### Context
The final project for the Modern ML course involves solving a problem using the Lending Club Dataset. The objective is to build a binary classification model to predict the probability of default on a loan application.

### Instructions
Store these instructions inside `case/instructions/case_overview.md`.

1. **Dataset**
    - Use the Lending Club Dataset.
    - Download the train and test datasets from the provided drive link.
    - Refer to the model catalog for a description of the variables: [Model Catalog](https://docs.google.com/spreadsheets/d/14FaRVNdObbYPskGK5UF_MmNW9d3WMjF3biu9R0V2zzw).

2. **Objective**
    - Build a binary classification model to predict the probability of default on a loan application.

3. **Data Preparation**
    - Select appropriate variables from the dataset. Avoid columns with future dates; choose only features related to the loan application.
    - Perform feature engineering to create new relevant features.
    - Optionally, use external variables (e.g., macroeconomic indicators or sociodemographic data).

4. **Dataset Details**
    - The training dataset covers the years 2007 to 2017.
    - The test dataset target is not public and covers the year 2018.

5. **Model Evaluation**
    - This case will function like a Kaggle competition. Use the training dataset to build your model; it will be public, but the test set target will be private.
    - Create validation sets or use K-fold cross-validation with the training dataset.
    - The output (predictions for the test set) should be probabilities and submitted in parquet format.
    - The evaluation metric will be log loss, measuring the accuracy of the output probabilities.

6. **Presentation**
    - In the final week, teams will present their results, ranked by log loss.
    - Develop a policy to decide which customers to approve in the test dataset based on Expected Losses of the loan. The policy should be justified and presented with the model report/results.

### Expected Loss Calculation
Use the following Python pseudo code to compute Expected Losses:

```python
# Total amount to be paid for the loan
calibration_df['principal'] = calibration_df.loan_amnt * (1 + calibration_df.int_rate)

# Exposure at default ratio, percentage of the total amount due relative to the principal
calibration_df['ead'] = calibration_df['principal'] - calibration_df.total_pymnt
calibration_df['ead_ratio'] = calibration_df['ead'] / calibration_df['principal']

# Loss given default ratio, percentage of recovery relative to the total amount due
calibration_df['lgd_ratio'] = 1 - calibration_df['recoveries'] / calibration_df['ead']

# Losses
calibration_df['losses'] = calibration_df['principal'] - calibration_df.total_pymnt + calibration_df['recoveries']
```

Keep everything in English.