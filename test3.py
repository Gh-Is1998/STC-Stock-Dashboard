
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go # type: ignore

st.title("STC Dashboard")
df_clean = pd.read_csv("stc.csv")

# تحويل التاريخ
df_clean['Date'] = pd.to_datetime(df_clean['Date'])
df_clean.set_index("Date", inplace=True)

# حساب MA
df_clean['MA20'] = df_clean['Close'].rolling(20).mean()
df_clean['MA50'] = df_clean['Close'].rolling(50).mean()

# حساب RSI
window = 14
delta = df_clean['Close'].diff()
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)
avg_gain = gain.rolling(window).mean()
avg_loss = loss.rolling(window).mean()
rs = avg_gain / avg_loss
df_clean['RSI'] = 100 - (100 / (1 + rs))

# ===== الرسم =====
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_clean.index,
    y=df_clean['Close'],
    name="Close"
))

fig.add_trace(go.Scatter(
    x=df_clean.index,
    y=df_clean['MA20'],
    name="MA20"
))

st.plotly_chart(fig, use_container_width=True)