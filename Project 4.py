import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("C:/Users/Public.LAPTOP-JGG5TD2E/Downloads/Dataset for Data Analytics.xlsx")

# Style
sns.set(style="whitegrid")

# Histogram
plt.figure(figsize=(8,5))
sns.histplot(df["TotalPrice"], bins=20, kde=True)
plt.title("Distribution of Total Price")
plt.show()

# Bar Chart - Order Status
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="OrderStatus", order=df["OrderStatus"].value_counts().index)
plt.title("Orders by Status")
plt.xticks(rotation=30)
plt.show()

# Bar Chart - Sales by Category
sales = df.groupby("Product")["TotalPrice"].sum().sort_values()

plt.figure(figsize=(8,5))
sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.show()

# Pie Chart
df["PaymentMethod"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.show()

# Box Plot
plt.figure(figsize=(8,5))
sns.boxplot(x=df["TotalPrice"])
plt.title("Box Plot of Total Price")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
sns.scatterplot(data=df,
                x="UnitPrice",
                y="TotalPrice")

plt.title("Unit Price vs Total Price")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8,6))

numeric = df.select_dtypes(include=["int64","float64"])

sns.heatmap(numeric.corr(),
            annot=True,
            cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

# Daily Sales Trend
daily = df.groupby("Date")["TotalPrice"].sum()

plt.figure(figsize=(12,5))
daily.plot()

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()
