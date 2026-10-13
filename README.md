# Customer Churn Prediction

A machine learning project focused on predicting customer churn
using classification algorithms.

## Overview

The goal is to identify customers who are likely to discontinue
their service.

This project explores data preprocessing, class imbalance,
classification metrics, and model evaluation.

## Machine Learning Workflow

- Data cleaning and missing-value handling
- Binary encoding and one-hot encoding
- Numerical feature scaling
- Train-test splitting
- SMOTENC for handling class imbalance
- Classification model training and comparison
- Decision threshold experimentation

## Models Explored

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

## Evaluation

Recall is a primary metric because the objective is to identify
as many actual churners as possible.

Other metrics include:

- Precision
- F1-score
- ROC-AUC
- Accuracy

## Current Status

- [x] Data preprocessing
- [x] Model experimentation
- [x] SMOTENC experiment
- [x] Classification threshold experiments
- [ ] FastAPI integration
- [ ] Docker integration
- [ ] Further model improvements

## Future Improvements

- Cross-validation and hyperparameter tuning
- Improved threshold selection
- Model pipeline optimization
- API deployment using FastAPI and Docker