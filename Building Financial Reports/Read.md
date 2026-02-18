# 💰 Building Financial Reports: Profitability & Leverage Analysis

## 📌 Project Overview
In this project, we step into the role of a **Financial Analyst at a hedge fund** to evaluate company performance across multiple industries.  
The focus is on understanding whether **highly leveraged real estate companies** tend to be more profitable — a key question for investment decisions.

Using financial statements data, we compute and analyze **leverage** and **profitability** ratios and visualize their relationship to support data-driven investing.

---

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
