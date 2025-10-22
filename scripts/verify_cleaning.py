# 

import pandas as pd
import numpy as np

CLEAN_PATH = "data/amazon_cleaned.csv"
SUMMARY_PATH = "data/amazon_summary.csv"

def check_cleaned_data():
    print("Checking cleaned dataset\n")
    df = pd.read_csv(CLEAN_PATH)

    print("Shape:", df.shape)
    print("\nData types:\n", df.dtypes)

    # 1. Check numeric columns

    numeric_cols = [
        "discounted_price", "actual_price", "discount_percentage",
        "rating", "rating_count", "price_difference"
    ]
    numeric_ok = all(np.issubdtype(df[c].dtype, np.number) for c in numeric_cols)
    print("\nNumeric columns correctly typed:", numeric_ok)


    # 2. Missing values
    print("\nMissing values per column:\n", df.isnull().sum())


    # 3. Logical constraints
    invalid_prices = df[df["discounted_price"] > df["actual_price"]]
    print(f"\nRows with invalid prices (> actual): {len(invalid_prices)}")

    neg_discounts = df[df["discount_percentage"] < 0]
    print(f"Rows with negative discount %: {len(neg_discounts)}")


    # 4. Category check
    if "category_clean" in df.columns:
        print("\nTop categories:")
        print(df["category_clean"].value_counts().head())
    else:
        print("\n 'category_clean' column missing!")


    # 5. Quick sample check
    print("\nSample rows:")
    print(df.sample(3)[["product_name", "actual_price", "discounted_price", "discount_percentage", "rating"]])

    print("\n Cleaning verification complete.\n")


def check_summary_data():
    print("\n\n Checking summary dataset\n")
    df = pd.read_csv(SUMMARY_PATH)

    print("Shape:", df.shape)
    print(df.head())

 
    if all(col in df.columns for col in ["avg_rating", "avg_discount_pct", "review_volume"]):
        print("\nSummary columns OK.")
        print(df.describe())
    else:
        print("\nMissing expected summary columns.")


if __name__ == "__main__":
    check_cleaned_data()
    print("=" * 80)
    check_summary_data()
