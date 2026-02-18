# 💰 Building Financial Reports: Profitability & Leverage Analysis

## 📌 Project Overview
In this project, we step into the role of a **Financial Analyst at a hedge fund** to evaluate company performance across multiple industries.  
The focus is on understanding whether **highly leveraged real estate companies** tend to be more profitable — a key question for investment decisions.

Using financial statements data, we compute and analyze **leverage** and **profitability** ratios and visualize their relationship to support data-driven investing.

A debt-to-equity ratio or an equity multiplier ratio. Save this ratio in a column named "leverage_ratio" in a DataFrame called df_ratios.

A gross margin ratio or an operating margin ratio. Save this ratio in a column named "profitability_ratio", in a DataFrame called df_ratios.

The datasets provided to you have information on the type of industry a company belongs to in a column called comp_type. Your manager also needs you to answer these three questions:

1) Which company type (comp_type) has the lowest profitability ratio? Save this comp_type value as a string in a variable called lowest_profitability.

2) Which company type has the highest leverage ratio? Save this comp_type value as a string in a variable called highest_leverage.

3) What is the relationship between leverage and profitability in the real estate companies represented in this data? Is it "positive," "negative," or "no relationship?" Save one of these three strings in a variable called relationship.


## Business Objective
Help the investment manager answer:
- Which industries are the most and least profitable?
- Which industries rely the most on leverage?
- Does higher leverage correlate with higher profitability in **real estate companies**?

---

## Dataset Information
The dataset contains company-level financial data, including:
- Balance sheet metrics
- Income statement metrics
- Industry classification

### Key Column
| Column Name | Description |
|------------|-------------|
| `comp_type` | Industry type of the company |

---

## Ratios Computed
Two core financial ratios were calculated and stored in a DataFrame named `df_ratios`.

### Leverage Ratio
Used to measure how much debt a company uses relative to equity.

- Examples:
  - **Debt-to-Equity Ratio**
  - **Equity Multiplier**

Saved as:
```python
df_ratios["leverage_ratio"]


