import pandas as pd

df = pd.read_csv("data/raw/telco_churn.csv")
df["c"] = df["Churn"] == "Yes"

print("Contract counts:")
print(df["Contract"].value_counts())

print("\nChurn by Contract:")
print(df.groupby("Contract")["c"].agg(["count", "mean"]))

churned = df[df["c"]]
print("\nChurned customers by PaymentMethod (count, share of churned):")
print(churned["PaymentMethod"].value_counts())
print(churned["PaymentMethod"].value_counts(normalize=True))

print("\nShare of ALL customers by PaymentMethod:")
print(df["PaymentMethod"].value_counts(normalize=True))

print("\nChurn rate by PaymentMethod:")
print(df.groupby("PaymentMethod")["c"].agg(["count", "mean"]))

m = df["MonthlyCharges"].min()
df["bin"] = (m + ((df["MonthlyCharges"] - m) // 10) * 10).round(2)
print("\nChurn by MonthlyCharges band (10 wide, starting at the minimum):")
print(df.groupby("bin")["c"].agg(["count", "mean"]))

print("\nFiber vs DSL churn within each contract:")
sub = df[df["InternetService"].isin(["DSL", "Fiber optic"])]
print(sub.groupby(["Contract", "InternetService"])["c"].agg(["count", "mean"]))