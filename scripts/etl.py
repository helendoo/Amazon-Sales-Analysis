import sys
from datetime import datetime
import pandas as pd


def clean_prices(series: pd.Series) -> pd.Series:
    return (
        series.astype(str)
              .str.replace(r"[^\d\.]", "", regex=True)
              .replace("", pd.NA)
              .astype(float)
    )


def build_category_clean(series: pd.Series) -> pd.Series:
    """Take last level from the 'category' path for nicer charts."""
    return series.astype(str).str.split("|").str[-1].str.strip()


def main(src="data/amazon.csv",
         dst_clean="data/amazon_cleaned.csv",
         dst_summary="data/amazon_summary.csv"):

    # 1) Load
    df = pd.read_csv(src)

    # 2) Convert types
    df["discounted_price"] = clean_prices(df["discounted_price"])
    df["actual_price"] = clean_prices(df["actual_price"])
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df["rating_count"] = pd.to_numeric(df["rating_count"], errors="coerce")

    # 3) Handle small amount of missing values
    if df["rating"].isna().any():
        df["rating"] = df["rating"].fillna(df["rating"].mean())
    df["rating_count"] = df["rating_count"].fillna(0)

    # 4) Recompute discount percentage 
 
    valid_price_mask = (df["actual_price"] > 0) & (df["discounted_price"] >= 0)
    df = df[valid_price_mask].copy()
    df["discount_percentage"] = (
        (df["actual_price"] - df["discounted_price"]) / df["actual_price"] * 100
    )

    
    df = df[df["discounted_price"] <= df["actual_price"]]

    # 5) Helper features for analysis & visuals
    df["price_difference"] = df["actual_price"] - df["discounted_price"]
    df["category_clean"] = build_category_clean(df["category"])


    # 6) de-duplication:

    if "product_id" in df.columns:
        df.sort_values(["product_id", "rating_count"], ascending=[True, False], inplace=True)
        df = df.drop_duplicates(subset="product_id", keep="first")

    # 7) Summary table 
    summary = (
        df.groupby("category_clean", dropna=False)
          .agg(
              products=("product_id", "nunique"),
              avg_price=("discounted_price", "mean"),
              avg_rating=("rating", "mean"),
              avg_discount_pct=("discount_percentage", "mean"),
              review_volume=("rating_count", "sum"),
          )
          .reset_index()
          .rename(columns={"category_clean": "category"})
          .sort_values("products", ascending=False)
    )

    # 8) Save outputs
    df.to_csv(dst_clean, index=False)
    summary.to_csv(dst_summary, index=False)

    # 9) Log
    with open("etl_log.txt", "a", encoding="utf-8") as f:
        f.write(
            f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
            f"Rows: {len(df)} | Categories: {summary['category'].nunique()} | "
            f"Saved -> {dst_clean}, {dst_summary}\n"
        )

    # Confirmation
    print(f"Cleaned rows: {len(df)}")
    print(f"Categories: {summary['category'].nunique()}")
    print("Files saved:", dst_clean, "and", dst_summary)


if __name__ == "__main__":
    src_arg = sys.argv[1] if len(sys.argv) > 1 else "data/amazon.csv"
    dst_clean_arg = sys.argv[2] if len(sys.argv) > 2 else "data/amazon_cleaned.csv"
    dst_summary_arg = sys.argv[3] if len(sys.argv) > 3 else "data/amazon_summary.csv"
    main(src_arg, dst_clean_arg, dst_summary_arg)
