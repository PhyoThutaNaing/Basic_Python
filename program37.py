import pandas as pd
import matplotlib.pyplot as plt

# Monthly sales data
data = {
    "Jan": 200,
    "Feb": 250,
    "Mar": 300,
    "Apr": 150,
    "May": 400,
    "Jun": 350
}

sales = pd.Series(data)

# Total sales
total_sales = sales.sum()
print("Total Sales:", total_sales)

# Highest selling month
max_month = sales.idxmax()
print("Highest Selling Month:", max_month)

# Pie chart (expenses = same data for simplicity)
plt.pie(sales, labels=sales.index, autopct='%1.1f%%')
plt.title("Monthly Expenses Pie Chart")
plt.show()
