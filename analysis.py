import pandas as pd

# Load dataset
df = pd.read_csv("data/churn.csv")

print("🔹 First 5 rows:")
print(df.head())

print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Columns:")
print(df.columns)


# -----------------------------
# Data Cleaning
# -----------------------------
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.dropna(inplace=True)


# -----------------------------
# Churn Analysis
# -----------------------------

# Churn Count
print("\n🔹 Churn Count:")
print(df["Churn"].value_counts())

# Churn Rate
churn_rate = df["Churn"].value_counts(normalize=True) * 100
print("\n🔹 Churn Rate (%):")
print(churn_rate)

# Insight
print("\n💡 Insight: Around {:.2f}% customers have churned.".format(churn_rate["Yes"]))


# -----------------------------
# Gender vs Churn
# -----------------------------
print("\n🔹 Churn by Gender:")
print(pd.crosstab(df["gender"], df["Churn"]))

print("\n💡 Insight: Compare churn distribution across genders.")


# -----------------------------
# Monthly Charges vs Churn
# -----------------------------
print("\n🔹 Avg Monthly Charges by Churn:")
print(df.groupby("Churn")["MonthlyCharges"].mean())

print("\n💡 Insight: Customers who churn tend to have higher monthly charges.")


# -----------------------------
# Tenure vs Churn
# -----------------------------
print("\n🔹 Avg Tenure by Churn:")
print(df.groupby("Churn")["tenure"].mean())

print("\n💡 Insight: Customers with lower tenure are more likely to churn.")


# -----------------------------
# Internet Service vs Churn
# -----------------------------
print("\n🔹 Churn by Internet Service:")
print(pd.crosstab(df["InternetService"], df["Churn"]))

print("\n💡 Insight: Fiber optic users often show higher churn.")