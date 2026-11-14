import pandas as pd

df = pd.read_csv("data/raw/telco_churn.csv")
df["c"] = df["Churn"] == "Yes"

print("Churn by PhoneService:")
print(df.groupby("PhoneService")["c"].agg(["count", "mean"]))

print("\nChurn by InternetService:")
print(df.groupby("InternetService")["c"].agg(["count", "mean"]))

services = ["OnlineSecurity", "OnlineBackup", "DeviceProtection",
            "TechSupport", "StreamingTV", "StreamingMovies"]
for s in services:
    print(f"\n{s}:")
    print(df.groupby(s)["c"].agg(["count", "mean"]))

df["ServiceCount"] = (df[services] == "Yes").sum(axis=1)
print("\nChurn by ServiceCount (all customers):")
print(df.groupby("ServiceCount")["c"].agg(["count", "mean"]))

print("\nChurn by ServiceCount (internet customers only):")
net = df[df["InternetService"] != "No"]
print(net.groupby("ServiceCount")["c"].agg(["count", "mean"]))

print("\nFiber investigation: average monthly charge")
print(df.groupby("InternetService")["MonthlyCharges"].mean())
print("\nContract mix within each internet type:")
print(pd.crosstab(df["InternetService"], df["Contract"], normalize="index"))