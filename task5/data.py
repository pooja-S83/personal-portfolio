import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Load CSV using Pandas ---

try:
    df = pd.read_csv('sales_data.csv') 
    print("CSV file loaded successfully.")
except FileNotFoundError:
    print("ERROR: 'sales_data.csv' not found. Creating a sample DataFrame for demonstration.")
    data = {
        'Order ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Product Category': ['Electronics', 'Furniture', 'Electronics', 'Apparel', 'Furniture', 'Electronics', 'Apparel', 'Furniture', 'Electronics', 'Apparel'],
        'Sales': [1200.50, 450.00, 800.25, 55.75, 120.50, 1500.00, 90.00, 300.00, 210.50, 40.00],
        'Region': ['North', 'South', 'North', 'East', 'West', 'South', 'East', 'North', 'West', 'North']
    }
    df = pd.DataFrame(data)


print("\n--- DataFrame Head and Info ---")
print(df.head()) 
print("\n", df.info())
print("DataFrame Shape (Rows, Columns):", df.shape)

sales_by_category = df.groupby('Product Category')['Sales'].sum()

print("\n--- Total Sales by Product Category ---")
print(sales_by_category)

# --- 3. plot() (Visualization) ---
# Create a Bar Chart
plt.figure(figsize=(10, 6))
sales_by_category.plot(
    kind='bar',             # Specifies a bar chart
    color='skyblue',
    edgecolor='black'
)

plt.title('Total Sales by Product Category (Task 5 Insight)', fontsize=15)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45, ha='right') 
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


print("\n--- Summary ---")
print(f"The highest selling category is: {sales_by_category.idxmax()} with ${sales_by_category.max():.2f}")
print(f"The lowest selling category is: {sales_by_category.idxmin()} with ${sales_by_category.min():.2f}")