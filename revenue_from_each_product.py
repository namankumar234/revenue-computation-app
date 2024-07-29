import pandas as pd

def compute_product_revenue(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Compute the revenue for each order
    df['revenue'] = df['product_price'] * df['quantity']

    # Group by 'product_id' and 'product_name' and compute the total revenue
    product_revenue = df.groupby(['product_id', 'product_name'])['revenue'].sum().reset_index()

    # Rename columns for clarity
    product_revenue.columns = ['Product ID', 'Product Name', 'Total Revenue']

    # Print the results
    print(product_revenue)

    product_revenue.to_csv('revenue_from_each_product.csv', index=False)
    
if __name__ == "__main__":
    file_path = 'orders.csv'
    compute_product_revenue(file_path)