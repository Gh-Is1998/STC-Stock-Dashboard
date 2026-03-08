import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("STC Dashboard 📊")


df_clean = pd.read_csv("stc.csv")

df = df_clean.copy()

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# اختيار السنة من القائمة
years = sorted(df['Date'].dt.year.dropna().unique())
selected_year = st.selectbox("select the year", years)

# فلترة حسب السنة
filtered = df[df['Date'].dt.year == selected_year]

# تحديد الألوان
colors = np.where(filtered['Close'] > filtered['Open'], 'green', 'red')

# رسم الحجم
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(filtered['Date'], filtered['Volume'], color=colors)

ax.set_title(f"STC Volume - {selected_year}")
ax.set_xlabel("Date")
ax.set_ylabel("Volume")
ax.grid(True)

st.pyplot(fig)       

                                                                                            

