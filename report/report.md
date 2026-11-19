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

- **Phone service** has little effect: 26.7% churn with phone service versus 24.9% without (only 682 customers have no phone service).
- **Internet type:** Fiber optic customers churn at 41.9% (3,096 customers), DSL at 19.0% (2,421), and customers with no internet at 7.4% (1,526).

**Which services are most strongly associated with higher churn?** Churn is highest for customers who lack protective services. Among internet customers, those without OnlineSecurity churn at 41.8% versus 14.6% with it, and those without TechSupport churn at 41.6% versus 15.2% with it, which are the two largest gaps (about 26-27 points). OnlineBackup (39.9% vs 21.5%) and DeviceProtection (39.1% vs 22.5%) show smaller gaps of roughly 17-18 points. StreamingTV and StreamingMovies barely matter: customers with them churn about 3-4 points less (30% vs 34%). These are associations, not proof that the services cause retention.

**How does ServiceCount affect churn?** Among internet customers, churn falls steadily as add-on services increase: 52.2% at 0 add-ons (693 customers), 45.8% at 1, 35.8% at 2, 27.4% at 3, 22.3% at 4, 12.4% at 5 and 5.3% at 6 (284 customers). Customers with no internet also have ServiceCount 0 but churn at only 7.4%, so the chart separates them by InternetService. Pooling them would show 21.4% at 0 add-ons and hide the trend. Customers with more services may also have longer tenure or contracts, so this doesn't prove that adding services reduces churn.

**Why do Fiber optic customers churn more?** Fiber customers pay an average of 91.50 per month versus 58.10 for DSL (about 57% more), and 68.7% of them are on month-to-month contracts versus 50.5% of DSL customers (only 13.9% are on two-year contracts versus 26.0%). Higher price and weaker contract commitment come bundled with Fiber, so the high churn can't be blamed on the technology alone. Holding contract type fixed (section 5), Fiber still churns more than DSL in every contract, though the gap narrows from 22 points on month-to-month to 5 points on two-year contracts. So contract mix alone does not explain Fiber's higher churn. Its higher price is another candidate that this analysis did not isolate.

## 5. Contract and billing

**Does contract length reduce churn, and by how much?** Yes, strongly. Month-to-month customers churn at 42.7% (3,875 customers), one-year customers at 11.3% (1,473) and two-year customers at 2.8% (1,695). One-year customers churn about 31 percentage points less than month-to-month customers, and two-year customers about 40 points less, a rate roughly 15 times lower. This is an association: customers who plan to stay may simply choose longer contracts in the first place.

**Is any payment method disproportionately represented among churned customers?** Yes, electronic check. It accounts for 57.3% of churned customers (1,071 of 1,869) but only 33.6% of all customers, about 1.7 times its share. Its own churn rate is 45.3% (of 2,365 customers), versus 19.1% for mailed check, 16.7% for bank transfer (automatic) and 15.2% for credit card (automatic). The other three methods are each under-represented among churned customers (12-17% of churners versus 22-23% of all customers). This analysis does not control for contract type or tenure, so it shows an association, not a cause.

**Monthly charges.** Churn does not rise smoothly with price (bands are 10 wide, labelled by their lower bound). The cheapest band (18.25, 1,606 customers) churns at only 9.2%. Bands from 68.25 to 98.25 all churn at 36-39%, and the 108.25 band falls back to 15.2% (310 customers). The 118.25 band has only 5 customers, too few to interpret. Price alone does not explain churn.

**Fiber versus DSL within each contract.** Holding contract type fixed, Fiber optic still churns more than DSL in every contract:

| Contract | DSL | Fiber optic | Gap |
|---|---|---|---|
| Month-to-month | 32.2% | 54.6% | 22.4 points |
| One year | 9.3% | 19.3% | 10.0 points |
| Two year | 1.9% | 7.2% | 5.3 points |

## 6. Tenure and churn

The dataset is a snapshot, so these figures compare customers at different tenures. They do not follow the same customers over time.

| Tenure | Month-to-month | One year | Two year | All contracts |
|---|---|---|---|---|
| 0-12 months | 51.4% (1,994) | 10.5% (124) | 0.0% (68) | 47.4% (2,186) |
| 13-24 months | 37.7% (737) | 8.1% (197) | 0.0% (90) | 28.7% (1,024) |
| 25-48 months | 32.9% (802) | 10.6% (518) | 2.2% (274) | 20.4% (1,594) |
| 49+ months | 26.0% (342) | 12.9% (634) | 3.3% (1,263) | 9.5% (2,239) |

Churn rate, with customer count in brackets.

**At what point is churn risk highest?** In the first months of the relationship. Month 1 is the peak: 62.0% of customers with one month of tenure have churned (613 customers). The rate then falls to 51.7% at month 2, about 47-48% at months 3-5, and 31-39% from months 6 to 12. In the 6-month histogram bins, the 0-5 month bin has the most churned customers of any bin (744 churned versus 627 retained, 54.3% churn).

**Are long-tenure customers less likely to churn, and does the effect hold once you control for contract type?** Overall, yes: churn falls from 47.4% in the first year to 9.5% after 49 months. Once contract type is controlled, the effect holds only for month-to-month customers (51.4% falling to 26.0%). For one-year customers the rate does not fall (10.5%, 8.1%, 10.6%, 12.9%). For two-year customers it is close to zero at every tenure: none of the 158 customers with under 24 months of tenure churned, and the rate reaches only 3.3% at 49+ months. Part of the overall tenure effect is therefore a contract-mix effect: 84.7% of customers with 49+ months of tenure are on one- or two-year contracts (1,897 of 2,239), compared with 8.8% of customers in their first year (192 of 2,186). Contract type matters at every tenure level, while tenure matters mainly within month-to-month. Even month-to-month customers with 49+ months churn at 26.0%, against 3.3% for two-year customers of the same tenure. These are associations, not proof of cause.

## 7. Interactivity

Four dropdown slicers (Contract, InternetService, PaymentMethod, Churn) sit at the bottom of every page and are synced, so a selection filters every visual on every page. I tested this: Contract = Month-to-month shows 3,875 customers at a 42.71% churn rate, and adding InternetService = Fiber optic shows 2,128 customers at 54.61%, both matching the Python checks. Every chart has a tooltip showing the exact churn rate and customer count. Four calculated measures were added and checked against Python: average tenure of churned customers (17.98 months), average monthly charge of churned customers (74.44), the share of customers with both OnlineSecurity and TechSupport (15.6%), and the share with both streaming services (27.5%). The first two always describe churned customers, so they ignore the Churn slicer by design.