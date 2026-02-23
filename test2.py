import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go # pyright: ignore[reportMissingImports]

st.title("STC Interactive Dashboard 📈")

# قراءة الملف
df_clean = pd.read_csv("stc.csv")

# تحويل التاريخ
df_clean['Date'] = pd.to_datetime(df_clean['Date'], errors='coerce')
df_clean = df_clean.sort_values("Date")
df_clean.set_index("Date", inplace=True)

# حساب المتوسطات

df_clean['MA20'] = df_clean['Close'].rolling(20).mean()
df_clean['MA50'] = df_clean['Close'].rolling(50).mean()
df_clean['MA200'] = df_clean['Close'].rolling(200).mean()

# إشارات مباشرة بدون slicing
df_clean['Signal'] = np.where(
    df_clean['MA20'] > df_clean['MA50'],
    1,
    -1
)
# إشارات
df_clean['Signal'] = np.where(
    df_clean['MA20'] > df_clean['MA50'],
    1,
    -1
)
# ===== الرسم التفاعلي =====
fig = go.Figure()

# السعر
fig.add_trace(go.Scatter(
    x=df_clean.index,
    y=df_clean['Close'],
    mode='lines',
    name='Close Price'
))

# المتوسطات
fig.add_trace(go.Scatter(x=df_clean.index, y=df_clean['MA20'], name='MA20'))
fig.add_trace(go.Scatter(x=df_clean.index, y=df_clean['MA50'], name='MA50'))
fig.add_trace(go.Scatter(x=df_clean.index, y=df_clean['MA200'], name='MA200'))

# إشارات شراء
fig.add_trace(go.Scatter(
    x=df_clean[df_clean['Signal']==1].index,
    y=df_clean[df_clean['Signal']==1]['Close'],
    mode='markers',
    marker=dict(symbol="triangle-up", size=10, color="green"),
    name="Buy"
))

# إشارات بيع
fig.add_trace(go.Scatter(
    x=df_clean[df_clean['Signal']==-1].index,
    y=df_clean[df_clean['Signal']==-1]['Close'],
    mode='markers',
    marker=dict(symbol="triangle-down", size=10, color="red"),
    name="Sell"
))

fig.update_layout(
    template="plotly_dark",
    title="STC Stock with Moving Averages",
    xaxis_title="Date",
    yaxis_title="Price"
)

st.plotly_chart(fig, use_container_width=True)