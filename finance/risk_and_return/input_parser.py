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
        'ExpectedReturn': asset_risk.expected_return, 
        'InvVol': asset_risk.inverse_volatility
    })

stats_df = pd.DataFrame(asset_stats)

# derive weights (normalization)
stats_df['Weight'] = stats_df['InvVol'] / stats_df['InvVol'].sum()

weights_vector = stats_df['Weight'].values
# Find daily return of whole portfolio
portfolio_daily_return = returns_df.dot(weights_vector)
#Add to cumulative returns for line graph
cum_returns = (1 + returns_df).cumprod()
cum_returns['PORTFOLIO'] = (1 + portfolio_daily_return).cumprod()


#######----PLOTS----#####==============================================================================================
# Part II
# Create a heatmap
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


#Part IV
#shows each shs invested in 1 stock
# Calculate cumulative returns: (1 + r).cumprod()
cum_returns = (1 + returns_df).cumprod()
# Calculate Portfolio Return (using your derived weights)
weights_array = stats_df['Weight'].values
portfolio_daily_return = (returns_df * weights_array).sum(axis=1)
cum_returns['MY_PORTFOLIO'] = (1 + portfolio_daily_return).cumprod()

plt.figure(figsize=(12, 6))
for col in cum_returns.columns:
    linewidth = 4 if col == 'MY_PORTFOLIO' else 1.5
    plt.plot(cum_returns[col], label=col, lw=linewidth)

plt.title('Growth of 1 Kshs Investment: Stocks vs. Optimized Portfolio')
plt.legend()
plt.show()


#Part V
# Risk-Return scatter
plt.figure(figsize=(10, 6))
# Plot individual assets
plt.scatter(stats_df['StdDev'], stats_df['ExpectedReturn'], s=100, alpha=0.6)
# Plot the Portfolio point 
# This shows the portfolio is smarter than individual assets investment
port_return = portfolio_daily_return.mean()
port_risk = portfolio_daily_return.std()
plt.scatter(port_risk, port_return, color='red', marker='*', s=300, label='Optimized Portfolio')
plt.xlabel('Risk (Standard Deviation)')
plt.ylabel('Return (Mean Daily)')
plt.title('Risk vs. Return: The Power of Weights')
plt.legend()
plt.show()


#Part VII
# shows how risk changes over time. Proves the portfolio stays calmer during shocks compared to single stocks.
# Rolling Volatility(Stability Chart)
# 20-day rolling standard deviation
returns_df.rolling(window=20).std().plot(figsize=(12,6))
plt.title('20-Day Rolling Volatility (Market Turbulence)')
plt.show()

#========================================================================================================================

# All in 1
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style to look more 'financial'
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('Portfolio Construction Analysis: Inverse Volatility Strategy', fontsize=20, fontweight='bold')

# --- 1. Top Left: Cumulative Returns (Growth of $1) ---
for col in cum_returns.columns:
    width = 4 if col == 'MY_PORTFOLIO' else 1.2
    alpha = 1 if col == 'MY_PORTFOLIO' else 0.6
    axes[0, 0].plot(cum_returns[col], label=col, lw=width, alpha=alpha)
axes[0, 0].set_title('Growth of $1 Investment', fontsize=14)
axes[0, 0].legend(loc='upper left', fontsize=8)
axes[0, 0].set_ylabel('Value ($)')

# --- 2. Top Right: Correlation Heatmap ---
sns.heatmap(returns_df.corr(), annot=True, cmap='RdYlGn', ax=axes[0, 1], center=0, fmt=".2f")
axes[0, 1].set_title('Asset Correlation Matrix (Interactive Risk)', fontsize=14)

# --- 3. Bottom Left: Risk vs Return Scatter ---
axes[1, 0].scatter(stats_df['StdDev'], stats_df['ExpectedReturn'], s=150, alpha=0.5, color='blue')
# Add Portfolio Point
port_return = portfolio_daily_return.mean()
port_risk = portfolio_daily_return.std()
axes[1, 0].scatter(port_risk, port_return, color='red', marker='*', s=400, label='Our Portfolio')
# Annotate Assets
for i, txt in enumerate(stats_df['Ticker']):
    axes[1, 0].annotate(txt, (stats_df.StdDev[i], stats_df.ExpectedReturn[i]), xytext=(5,5), textcoords='offset points')
axes[1, 0].set_title('The Efficient Frontier: Risk vs Return', fontsize=14)
axes[1, 0].set_xlabel('Volatility (Daily Std Dev)')
axes[1, 0].set_ylabel('Mean Daily Return')
axes[1, 0].legend()

# --- 4. Bottom Right: Portfolio Allocation Pie ---
axes[1, 1].pie(stats_df['Weight'], labels=stats_df['Ticker'], autopct='%1.1f%%', 
             startangle=140, colors=sns.color_palette('viridis', len(stats_df)))
axes[1, 1].set_title('Final Weight Allocation (Inverse Volatility)', fontsize=14)

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust for suptitle
plt.show()
