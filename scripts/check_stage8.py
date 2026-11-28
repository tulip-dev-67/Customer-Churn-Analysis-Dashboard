import pandas as pd

df = pd.read_csv("data/raw/telco_churn.csv")
df["c"] = df["Churn"] == "Yes"
services = ["OnlineSecurity", "OnlineBackup", "DeviceProtection",
            "TechSupport", "StreamingTV", "StreamingMovies"]
labels = ["Security", "Backup", "Protection", "Support", "TV", "Movies"]


def combo(row):
    if row["InternetService"] == "No":
        return "No internet"
    picked = [lab for col, lab in zip(services, labels) if row[col] == "Yes"]
    return " + ".join(picked) if picked else "Internet only"


df["ServiceCombo"] = df.apply(combo, axis=1)
counts = df[df["c"]]["ServiceCombo"].value_counts()
pareto = pd.DataFrame({
    "churned": counts,
    "cum_share": (counts.cumsum() / counts.sum()).round(3),
})
print("Top 10 service combinations among churned customers:")
print(pareto.head(10))
print("Distinct combinations among churned:", len(counts))

df["bucket"] = pd.cut(df["tenure"], bins=[-1, 12, 24, 48, float("inf")],
                      labels=["0-12", "13-24", "25-48", "49+"])
df["ServiceCount"] = (df[services] == "Yes").sum(axis=1)
print("\nCohorts by TenureBucket:")
print(df.groupby("bucket", observed=True).agg(
    customers=("c", "size"),
    churn_rate=("c", "mean"),
    avg_monthly=("MonthlyCharges", "mean"),
    avg_service_count=("ServiceCount", "mean"),
).round(3))

print("\nService uptake by cohort (share of customers with the service):")
print((df[services] == "Yes").groupby(df["bucket"], observed=True).mean().T.round(3))

print("\nCandidate high-risk segments:")
seg1 = df[(df["Contract"] == "Month-to-month")
          & (df["InternetService"] == "Fiber optic")
          & (df["tenure"] <= 12)]
seg2 = seg1[(seg1["OnlineSecurity"] == "No") & (seg1["TechSupport"] == "No")]
seg3 = seg2[seg2["PaymentMethod"] == "Electronic check"]
total_churned = df["c"].sum()
for name, seg in [
    ("Month-to-month + Fiber + first year", seg1),
    ("... and no Security or Support", seg2),
    ("... and electronic check", seg3),
]:
    print(name, "| customers:", len(seg),
          "| churn rate:", round(seg["c"].mean(), 3),
          "| share of all churners:", round(seg["c"].sum() / total_churned, 3))