import pandas as pd

df = pd.read_csv("data/raw/telco_churn.csv")
df["c"] = df["Churn"] == "Yes"

print("Churned by gender:")
print(df.groupby("gender")["c"].agg(["sum", "mean"]))

print("\nChurn rate by SeniorCitizen (0 = No, 1 = Yes):")
print(df.groupby("SeniorCitizen")["c"].mean())

print("\nChurn rate by Partner and Dependents:")
print(df.groupby(["Partner", "Dependents"])["c"].agg(["count", "mean"]))

print("\nChurn rate by Dependents only:")
print(df.groupby("Dependents")["c"].mean())