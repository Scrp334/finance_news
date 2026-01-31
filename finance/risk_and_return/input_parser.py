import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from risk import Risk

#Part I
# Load data
df = pd.read_excel("/home/rev/Desktop/data_analysis/data_for_test.xlsx")

#Calculate daily returns (The foundation for risk/return)
# This converts prices into percentage changes
returns_df = df.iloc[:, 1:].pct_change().dropna()

#Use "Risk" class to get stats for each asset
asset_stats = []
for col in returns_df.columns:
    # Assuming daily probabilities are equal (1/n)
    probs = [1/len(returns_df)] * len(returns_df)

    # Initialize the class
    asset_risk = Risk(probs, returns_df[col].tolist())
    
    asset_stats.append({
        'Ticker': col,
        'StdDev': asset_risk.std_dev,
        'InvVol': asset_risk.inverse_volatility
    })

stats_df = pd.DataFrame(asset_stats)

# derive weights (normalization)
stats_df['Weight'] = stats_df['InvVol'] / stats_df['InvVol'].sum()


# Part II
plt.figure(figsize=(10, 8))
sns.heatmap(returns_df.corr(), annot=True, cmap='RdYlGn', center=0)
plt.title('Asset Correlation Matrix (NSE Stocks)')
plt.show() 

#Part III
# Create a pie chart of weights
plt.figure(figsize=(8, 8))
plt.pie(stats_df['Weight'], labels=stats_df['Ticker'], autopct='%1.1f%%')
plt.title('Final Portfolio Weights (Inverse Volatility Strategy)')
plt.show()