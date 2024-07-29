import pandas as pd

def compute_top_10_customers(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Compute the revenue for each order
    df['revenue'] = df['product_price'] * df['quantity']

    # Group by 'customer_id' and compute the total revenue
    customer_revenue = df.groupby('customer_id')['revenue'].sum().reset_index()

    # Rename columns for clarity
    customer_revenue.columns = ['Customer ID', 'Total Revenue']

    # Sort customers by 'Total Revenue' in descending order
    top_customers = customer_revenue.sort_values(by='Total Revenue', ascending=False)

    # Select the top 10 customers
    top_10_customers = top_customers.head(10)

    # Print the results
    print(top_10_customers)

    top_10_customers.to_csv('top_10_customers.csv', index=False)


if __name__ == "__main__":
    file_path = 'orders.csv'
    compute_top_10_customers(file_path)