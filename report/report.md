# Telco Customer Churn Dashboard: Report

## 1. Data and ground truth

Source: Telco Customer Churn CSV, checked in Python before loading into Power BI.

| Check | Value |
|---|---|
| Rows / columns | 7,043 / 21 |
| Blank TotalCharges rows | 11 (all tenure = 0, all Churn = No) |
| Customers churned | 1,869 |
| Overall churn rate | 26.54% |
| Average monthly charge | 64.76 |

The Power BI summary cards match these figures exactly.

## 2. Cleaning decisions

- **TotalCharges** was stored as text. I converted it to a decimal number. The 11 blank rows are new customers with tenure 0 who haven't been billed yet, so I imputed 0. That is their true amount billed, not an invented value, and it keeps all 7,043 customers so totals match the source.
- **SeniorCitizen** was 0/1. I standardised it to No/Yes to match the other binary fields.
- **Three-state service fields** ("No internet service", and "No phone service" for MultipleLines) are kept as separate values. Collapsing them into No would distort churn rates, because customers with no internet churn at a very different rate from customers who declined an add-on.
- **ServiceCount** counts the six add-on services (OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies), so it ranges from 0 to 6.
- **AvgMonthlyValue** is TotalCharges / tenure, returning null when tenure = 0 to avoid division by zero.

## 3. Demographics and churn

- Gender: 939 female and 930 male customers churned (26.9% vs 26.2% churn rate), so there is almost no gender effect.
- Senior citizens churn at 41.7% versus 23.6% for non-seniors.

**Is there a relationship between dependents and churn?** Yes. Customers with dependents churn at 15.5% versus 31.3% for those without, roughly half the rate. The gap holds within both Partner groups (21.3% vs 34.2% among customers without a partner; 14.2% vs 25.4% among those with one), so it is not just a partner effect. This shows association, not cause, because households with dependents may also differ in contract type or age.

## 4. Service usage and churn

(to fill in after running scripts/check_services.py)

- Which services are most strongly associated with higher churn?
- How does ServiceCount affect churn?
- Why do Fiber optic customers churn more?