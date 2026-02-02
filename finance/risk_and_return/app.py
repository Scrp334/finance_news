import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from returns import Returns 
from risk import Risk

st.set_page_config(page_title="NSE Quant Dashboard", layout="wide")

st.title(" Portfolio Optimizer")
st.markdown("### Inverse Volatility Weighting Strategy")

# 1. Sidebar for Data Upload
uploaded_file = st.sidebar.file_uploader("Upload your NSE CSV or Excel", type=["csv","xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    # Ensure date is col 0
    df.iloc[:,0] = pd.to_datetime(df.iloc[:,0])
    df = df.set_index(df.columns[0])
    # find daily returns
    returns_df = df.iloc[:, 1:].pct_change().dropna() 
    
    # 2. Asset Selection
    selected_assets = st.sidebar.multiselect("Select Assets", returns_df.columns.tolist(), default=returns_df.columns.tolist())
    
    if selected_assets:
        filtered_returns = returns_df[selected_assets]
        
        # 3. Calculations (Using your logic)
        asset_stats = []
        for col in filtered_returns.columns:
            probs = [1/len(filtered_returns)] * len(filtered_returns)
            r_instance = Risk(probs, filtered_returns[col].tolist())
            asset_stats.append({
                'Ticker': col,
                'StdDev': r_instance.std_dev,
                'ExpectedReturn': r_instance.expected_return,
                'InvVol': r_instance.inverse_volatility
            })
        
        stats_df = pd.DataFrame(asset_stats)
        stats_df['Weight'] = stats_df['InvVol'] / stats_df['InvVol'].sum()
        
        # Portfolio Performance
        weights_vector = stats_df['Weight'].values
        portfolio_daily_return = filtered_returns.dot(weights_vector)
        
        # --- UI LAYOUT ---
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Portfolio Weights")
            fig_pie = px.pie(stats_df, values='Weight', names='Ticker', hole=0.4, color_discrete_sequence=px.colors.sequential.Viridis)
            st.plotly_chart(fig_pie)

        with col2:
            st.subheader("Correlation Heatmap")
            corr = filtered_returns.corr()
            fig_corr = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r')
            st.plotly_chart(fig_corr)

        st.subheader("Growth of $1: Portfolio vs Assets")
        cum_returns = (1 + filtered_returns).cumprod()
        cum_returns['MY_PORTFOLIO'] = (1 + portfolio_daily_return).cumprod()
        st.line_chart(cum_returns)

        

        # Download Button for Results
        st.download_button("Download Weights CSV", stats_df.to_csv().encode('utf-8'), "weights.csv", "text/csv")