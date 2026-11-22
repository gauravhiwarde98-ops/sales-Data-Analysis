import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/sales.csv")

# Display Data
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Statistical Analysis
print("\nStatistical Analysis:")
print(df.describe())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Product Wise Sales
product_sales = df.groupby("Product")["Sales"].sum()

print("\nProduct Wise Sales:")
print(product_sales)

# Visualization
sns.barplot(x=product_sales.index, y=product_sales.values)

plt.title("Product Wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Monthly Sales Analysis

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month_name()

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Monthly Sales Graph

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# City Wise Sales Analysis

city_sales = df.groupby("City")["Sales"].sum()

print("\nCity Wise Sales:")
print(city_sales)

# City Wise Graph

city_sales.plot(kind="bar")

plt.title("City Wise Sales Analysis")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

# City Wise Sales Analysis

city_sales = df.groupby("City")["Sales"].sum()

print("\nCity Wise Sales:")
print(city_sales)

# City Wise Sales Graph

plt.figure(figsize=(8, 5))

city_sales.plot(kind="bar")

plt.title("City Wise Sales Analysis")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

# Category Wise Sales Analysis

category_sales = df.groupby("Category")["Sales"].sum()

print("Category Wise Sales:")
print(category_sales)

# Visualization

category_sales.plot(
    kind="bar",
    title="Category Wise Sales Analysis"
)

plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Top 5 Selling Products

top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("Top 5 Selling Products:")
print(top_products)

# Visualization
plt.figure(figsize=(9, 5))

top_products.plot(kind="bar")

plt.title("Top 5 Selling Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Monthly Sales Analysis

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month_name()

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Monthly Sales Graph

plt.figure(figsize=(8, 5))

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# City Wise Sales Analysis

city_sales = df.groupby("City")["Sales"].sum()

print("City Wise Sales:")
print(city_sales)

plt.figure(figsize=(8, 5))

sns.barplot(x=city_sales.index, y=city_sales.values)

plt.title("City Wise Sales Analysis")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.show()
# Top Selling Product

product_sales = df.groupby("Product")["Sales"].sum()

top_product = product_sales.idxmax()
top_sales = product_sales.max()

print("Top Selling Product:", top_product)
print("Total Sales:", top_sales)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=product_sales.index,
    y=product_sales.values
)

plt.title("Top Selling Product Analysis")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()