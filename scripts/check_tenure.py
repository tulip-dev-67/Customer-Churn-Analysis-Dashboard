import pandas as pd

df = pd.read_csv("data/raw/telco_churn.csv")
df["c"] = df["Churn"] == "Yes"
df["bucket"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, float("inf")],
    labels=["0-12", "13-24", "25-48", "49+"],
)

print("Churn by TenureBucket:")
print(df.groupby("bucket", observed=True)["c"].agg(["count", "mean"]))

print("\nChurn by TenureBucket within each Contract:")
print(df.groupby(["Contract", "bucket"], observed=True)["c"].agg(["count", "mean"]))

df["bin6"] = (df["tenure"] // 6) * 6
print("\nCustomers by 6-month tenure bin and Churn:")
print(pd.crosstab(df["bin6"], df["Churn"]))

print("\nChurn rate by tenure month (first 12 months):")
print(df[df["tenure"] <= 12].groupby("tenure")["c"].agg(["count", "mean"]))