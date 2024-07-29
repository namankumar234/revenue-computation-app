import pandas as pd
def compute_monthly_revenue(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Ensure 'order_date' is in datetime format
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Compute the revenue for each order
    df['revenue'] = df['product_price'] * df['quantity']

    # Extract year and month from 'order_date'
    df['year_month'] = df['order_date'].dt.to_period('M')

    # Group by 'year_month' and compute the total revenue
    monthly_revenue = df.groupby('year_month')['revenue'].sum().reset_index()

    # Rename columns for clarity
    monthly_revenue.columns = ['Month', 'Total Revenue']

    # Print the results
    print(monthly_revenue)

    monthly_revenue.to_csv('revenue_for_each_month.csv', index=False)
    
if __name__ == "__main__":
    file_path = 'orders.csv'
    compute_monthly_revenue(file_path)