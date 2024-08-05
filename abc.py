import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'sonsale.csv'
data = pd.read_csv(file_path)

# Convert 'sale_date' to datetime
data['sale_date'] = pd.to_datetime(data['sale_date'], format='%m/%d/%Y')

# Plot 1: Total Sales over Time
plt.figure(figsize=(12, 6))
data.groupby('sale_date')['total_price'].sum().plot()
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Sales Distribution by Payment Method
plt.figure(figsize=(10, 6))
data['payment_method'].value_counts().plot(kind='bar')
plt.title('Sales Distribution by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Number of Sales')
plt.grid(True)
plt.tight_layout()
plt.show()


# Plot 4: Sales by Sale Channel
plt.figure(figsize=(10, 6))
data['sale_channel'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Sales by Sale Channel')
plt.ylabel('')
plt.grid(True)
plt.tight_layout()
plt.show()
