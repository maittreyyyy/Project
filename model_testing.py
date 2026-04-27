import joblib
import pandas as pd
import numpy as np
from pathlib import Path


MODEL_PATH = "lgbm_medicaid_model.pkl"
DATA_PATH = "df_model.csv"


def normalize_columns(df):
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def main():
    # -----------------------------
    # 1. Check files
    # -----------------------------
    if not Path(MODEL_PATH).exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

    if not Path(DATA_PATH).exists():
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")

    # -----------------------------
    # 2. Load model and data
    # -----------------------------
    print("Loading model...")
    model = joblib.load(MODEL_PATH)

    print("Loading test data...")
    df = pd.read_csv(DATA_PATH, low_memory=False)
    df = normalize_columns(df)

    print("Data shape:", df.shape)

    # -----------------------------
    # 3. Required features
    # -----------------------------
    feature_cols = [
        "year",
        "state",
        "quarter",
        "units_reimbursed",
        "number_of_prescriptions",
        "units_per_prescription",
        "therapeutic_class",
        "epc_class",
        "routename",
        "labelername",
        "marketingcategoryname",
        "is_expansion_state"
    ]

    missing = [col for col in feature_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # -----------------------------
    # 4. Clean and sample
    # -----------------------------
    df_test = df[feature_cols].dropna().copy()

    df_test = df_test.sample(
        n=min(10, len(df_test)),
        random_state=42
    )

    cat_cols = [
        "state",
        "therapeutic_class",
        "epc_class",
        "routename",
        "labelername",
        "marketingcategoryname",
        "is_expansion_state"
    ]

    for col in cat_cols:
        df_test[col] = df_test[col].astype("category")

    # -----------------------------
    # 5. Predict
    # -----------------------------
    print("Running predictions...")
    pred_log = model.predict(df_test)
    pred_cost_per_unit = np.expm1(pred_log)

    # -----------------------------
    # 6. Show results
    # -----------------------------
    results = df_test.copy()
    results["predicted_cost_per_unit"] = pred_cost_per_unit

    print("\nPrediction test successful.")
    print(results[[
        "year",
        "state",
        "quarter",
        "predicted_cost_per_unit"
    ]])


if __name__ == "__main__":
    main()