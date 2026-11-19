import pandas as pd

df = pd.read_csv("data/raw/telco_churn.csv")
churned = df[df["Churn"] == "Yes"]
print("Avg tenure, churned:", round(churned["tenure"].mean(), 2))
print("Avg monthly charge, churned:", round(churned["MonthlyCharges"].mean(), 2))
sec = ((df["OnlineSecurity"] == "Yes") & (df["TechSupport"] == "Yes")).mean()
stream = ((df["StreamingTV"] == "Yes") & (df["StreamingMovies"] == "Yes")).mean()
print("Share Security + Support:", round(sec * 100, 1), "%")
print("Share both Streaming:", round(stream * 100, 1), "%")