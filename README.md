# Amazon Sales & Review Analysis

A data analysis project using a public Amazon sales dataset from Kaggle.  
The data was cleaned and transformed in **Python (ETL workflow)** and visualized in **Power BI** to analyze relationships between **price, discounts, ratings, and product categories**.

---

## Project Structure
scripts/ → Python scripts for analysis, ETL, and validation
data/ → Contains the dataset (sample or cleaned CSVs)
dashboard/ → Power BI dashboard (.pbix file)
images/ → Dashboard screenshots

## Process Overview

### 1. Data Preparation (Python)
- Cleaned messy price and rating data  
- Handled missing and duplicate values  
- Calculated new features like 'discount_percentage' and 'price_difference'  
- Created summary statistics per product category  

### 2. Data Validation
- Verified column data types and logical consistency  
- Ensured valid price relationships (discounted ≤ actual price)  
- Checked for negative discounts or missing values  

### 3. Visualization (Power BI)
The final dashboard visualizes:
- **Average discount, rating, and review volume**
- **Price vs. rating correlation**
- **Top-rated product categories**
- **Most reviewed categories**
- **Category distribution (pie chart)**

---

### Price vs. Rating Correlation
No strong trend shows that cheaper products get better reviews. Ratings are consistent (3.5–4.5), suggesting performance matters more than price.

### Discount Effect
Large discounts (50–80%) don’t improve ratings. Moderate discounts (30–50%) show better balance between engagement and satisfaction.

### Category Performance
Top-rated categories: **Tablets**, **Basic**, **Coffee Presses**, **Cord Management**, **Film** (avg rating > 4.3).

### Review Count Distribution
Most-reviewed categories: **USB Cables**, **Remote Controls**, **Instant Water Heaters**, **Smart Watches** — indicating strong demand and frequent purchases.

For a detailed analysis and reasoning, see [Full Report](analysis_details.md).
