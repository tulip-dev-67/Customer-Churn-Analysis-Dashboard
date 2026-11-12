import pandas as pd

df = pd.read_csv("data/raw/telco_churn.csv")
print("Shape:", df.shape)
print("TotalCharges dtype:", df["TotalCharges"].dtype)

blank = df[df["TotalCharges"].str.strip() == ""]
print("Blank TotalCharges rows:", len(blank))
print("Their tenure values:", blank["tenure"].unique())
print("Their Churn values:", blank["Churn"].value_counts().to_dict())

print("SeniorCitizen values:", df["SeniorCitizen"].unique())
for col in ["OnlineSecurity", "MultipleLines", "InternetService"]:
    print(col, "->", df[col].unique())

print("Customers:", len(df))
print("Churned:", (df["Churn"] == "Yes").sum())
print("Churn rate:", round((df["Churn"] == "Yes").mean() * 100, 2), "%")
print("Avg monthly charge:", round(df["MonthlyCharges"].mean(), 2))