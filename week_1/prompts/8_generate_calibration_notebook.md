## Prompt

### About the Dataset
* It is a Machine Learning classification problem.
* The target variable is the 'churn_420' column.
* Here is the columns info() of the dataset:

### Task
Update and refactor the Python notebook at `./week_1/notebooks/8_calibration.ipynb` to perform the following tasks:

1. **Load the tuned model and test 3 calibrations (isotonic, Platt's scaling, and Venn-Abers):**
    - Load the tuned model from `./week_1/model/tunned_model.joblib`.
    - Use the `X_calibration` and `y_calibration` datasets for calibration.
    - Calibrate the model using Scikit-learn's Platt scaling (sigmoid).
    - Calibrate the model using Scikit-learn's isotonic regression.
    - Compute metrics for Platt scaling and isotonic regression using the `clf_metric_report` method.
    - Plot the calibration curve using the `plot_calibration_curve` function from the `utils.py` file.

2. **Calibrate the model using Venn-Abers:**
    - Adapt the following code example to use the tuned model:
      ```python
      clf.fit(X_train, y_train)
      p_cal = clf.predict_proba(X_calibration)
      p_test = clf.predict_proba(X_validation)

      va = VennAbersCalibrator()
      va_prefit_prob = va.predict_proba(p_cal=p_cal, y_cal=y_cal, p_test=p_test)
      ```
    - Make a final comparison using the baseline model, the feature selection model, and the tuned model with the calibrated models using Platt scaling, isotonic regression, and Venn-Abers calibration.
    - Compute metrics for Venn-Abers calibration using the `clf_metric_report` method.
    - Plot the calibration curve using the `plot_calibration_curve` function from the `utils.py` file.
    - List of models to load:
      - `./week_1/model/baseline_model.joblib`
      - `./week_1/model/tunned_model.joblib`
      - `./week_1/model/feat_selection_model.joblib`
