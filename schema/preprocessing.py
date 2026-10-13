from pathlib import Path

import joblib
import pandas as pd


# Resolve paths relative to the project root
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"


# Load saved preprocessing artifacts
scaler = joblib.load(MODEL_DIR / "scaler.pkl")
median = joblib.load(MODEL_DIR / "TC_median.pkl")

feature_columns = joblib.load(
    MODEL_DIR / "feature_columns.pkl"
)


# Columns encoded as Yes/No
BINARY_COLS = [
    "Partner",
    "Dependents",
    "PhoneService",
    "PaperlessBilling",
]


# Columns that were one-hot encoded during training
CATEGORICAL_COLS = [
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaymentMethod",
]


# Columns scaled during training
NUMERICAL_COLS = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
]


def preprocess_input(data: dict) -> pd.DataFrame:
    """
    Transform one validated customer record into the feature
    representation expected by the trained Logistic Regression.
    """

    df = pd.DataFrame([data])

    # Binary encoding
    for col in BINARY_COLS:
        df[col] = df[col].map({
            "Yes": 1,
            "No": 0,
        })

    # Gender encoding, Female=1 and Male=0
    df["gender"] = df["gender"].map({
        "Female": 1,
        "Male": 0,
    })

    # Converting TotalCharges to numeric and impute missing values
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce",
    )

    df["TotalCharges"] = df["TotalCharges"].fillna(median)

    # Scaling numerical columns using the fitted training scaler
    df[NUMERICAL_COLS] = scaler.transform(
        df[NUMERICAL_COLS]
    )

    # One-hot encoding remaining categorical columns
    df = pd.get_dummies(
        df,
        columns=CATEGORICAL_COLS,
        drop_first=True,
    )

    # Enforcing the exact feature columns and order used in training
    df = df.reindex(
        columns=feature_columns,
        fill_value=0,
    )

    return df