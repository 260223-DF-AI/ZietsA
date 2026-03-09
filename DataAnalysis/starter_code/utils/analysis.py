import pandas as pd

def load_data(filepath):
    """
    Load the orders dataset.
    - Parse dates correctly
    - Handle missing values
    - Return a clean DataFrame
    """
    df = pd.read_csv(filepath)
    df.dropna()
    return df

def explore_data(df):
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    print("="*30)
    print("  "*10 + "Data Report")
    print("="*30)
    print("- Shape:")
    rows, columns = df.shape # gets row and columns
    print(f"    - Rows: {rows}")
    print(f"    - Columns: {columns}")
    print(f"- Data Types:") 
    print(f"    {df.dtypes()}") # prints data types
    print(f"- Missing values count: {df.isna().sum().sum()}") # funds sum of is null dataframe
    print(f"- Date Range: {df["order_date"].min()} - {df["order_date"].max}") # shows from earlier to laters date
    print("="*30 + "\n")

def clean_data(df):
    """
    Clean the dataset:
    - Remove duplicates
    - Fill or drop missing values (document your strategy)
    - Standardize text columns (strip whitespace, consistent case)
    - Add calculated columns: 'total_amount' = quantity * unit_price
    """
    df.drop_duplicates() # drop duplicates
    df["total_amount"] = df["quantity"] * df["unit_price"] # get total_amount

def add_time_features(df):
    """
    Add time-based features:
    - day_of_week (0=Monday, 6=Sunday)
    - month
    - quarter
    - is_weekend (boolean)
    """
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    df["day_of_week"] = [days_of_week[day.weekday()] for day in df["order_date"]]
    df["is_weekend"] = df["day_of_week"] not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    df["month"] = df["order_date"].month()
    df["quarter"] = []
    for month in df["month"]:
        if month < 4:
            df["quarter"].append["Q1"]
        elif month < 7:
            df["quarter"].append["Q2"]
        elif month < 10:
            df["quarter"].append["Q3"]
        else:
            df["quarter"].append["Q4"]


def sales_by_category(df):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    new_df = df.groupby("category").agg(
        total_sales=("total_sales", "sum"),
        order_count=("total_sales", "count")
    )

    new_df["avg_order_value"] = new_df["total_sales"] / new_df["order_count"]
    
    return new_df

def sales_by_region(df):
    """
    Calculate total sales by region.
    Returns: DataFrame with columns [region, total_sales, percentage_of_total]
    """
    new_df = df.groupby("region")["total_sales"].sum()
    total = new_df["total_sales"].sum()
    new_df["percentage_of_total"] = new_df["total_sales"] / total

def top_products(df, n=10):
    """
    Find top N products by total sales.
    Returns: DataFrame with columns [product_name, category, total_sales, units_sold]
    """
    df.sort_values(by = "total_sales")
    return df.head(n)

def daily_sales_trend(df):
    """
    Calculate daily sales totals.
    Returns: DataFrame with columns [date, total_sales, order_count]
    """
    new_df = df.groupby("order_date").agg(
        total_sales=("total_sales", "sum"),
        order_count=("total_sales", "count")
    )
    return new_df

def customer_analysis(df):
    """
    Analyze customer purchasing behavior.
    Returns: DataFrame with columns [customer_id, total_spent, order_count, 
             avg_order_value, favorite_category]
    """
    new_df = df.groupby("customer_id").agg(
        total_sales=("total_sales", "sum"),
        order_count=("total_sales", "count"),
        favorite_category = ("category", "mode")
    )
    new_df["avg_order_value"] = new_df["total_sales"] / new_df["order_count"]
    return new_df

def weekend_vs_weekday(df):
    """
    Compare weekend vs weekday sales.
    Returns: Dict with weekend and weekday total sales and percentages.
    """
    total = df["total_sales"].sum()
    true_sum = df.query("is_weekend = True")["total_sales"].sum()
    false_sum =  true_sum = df.query("is_weekend = false")["total_sales"].sum()
    dictionary = {
        "weekend": {
            "total_sum": true_sum,
            "percentage": true_sum/total
        },
        "weekday": {
            "total_sum": false_sum,
            "percentage": false_sum/total
        }
    }
    return dictionary
