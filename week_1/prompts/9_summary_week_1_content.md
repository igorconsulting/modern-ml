## PROMPT:

Based on the workspace content and todo list, here's a summary of Week 1's content for the Machine Learning course:

## RESPONSE
Coletando informações do workspace

Based on the workspace content and todo list, here's a summary of Week 1's content for the Machine Learning course:

### Week 1: Churn Prediction for a Fintech Company

1. **Course Introduction & Setup**
- Course outline and schedule
- Communication channels setup (Discord, Email, LinkedIn)
- Overview of modern DS dev environment
  - Github
  - Visual Studio code
  - UV projects for package package and dependencies management
  - Using AI tools (like GitHub Copilot) for ML development
- Overview of modern DS tabular data stack
  - Gradient boosting with Catboost
  - Feature Engineering
  - ARFS for feature selection (Leshy Boruta)
  - Interpretability with SHAP and Permuation Importance
  - Evaluation Metrics (Brier Score and Logloss)
  - PR-AUC and Calibration curves
  - Traditional Calibration
  -  Venn Abber Predictor


1. **The Problem: Customer Churn Prediction**
- Binary classification problem
- Churn definition: Customer inactivity period > 365 days
- Dataset contains financial transaction data from 2008 to 2026
- Features include transaction amounts, customer info, and behavioral metrics

1. **Data Engineering & Feature Engineering**
- Temporal data splitting (Train/Validation/Test)
- Feature engineering techniques:
  - Window-based features (10D, 90D, 180D, 365D, 450D periods)
  - Transaction aggregations
  - Customer behavior metrics
  - Historical balance calculations

1. **Machine Learning Implementation**
- CatBoost model implementation
- Feature selection using ARFS (Leshy algorithm)
- Model calibration techniques
- Hyperparameter tuning with Optuna

1. **Model Evaluation & Interpretation**
- Key metrics:
  - Log loss
  - Precision-Recall AUC
  - ROC AUC
  - Brier score
- Model interpretability:
  - SHAP values
  - Permutation importance
- Calibration curves analysis

1. **Development Environment**
- Python environment setup with UV library
- Installation of key ML libraries:
  - pandas
  - catboost
  - seaborn
  - SHAP
  - fastshap
  - optuna
  - ARFS (Feature Selection for Boruta)
  - venn-abers

The content focuses on practical implementation while covering essential ML concepts, with emphasis on handling imbalanced data, model calibration, and interpretability techniques.