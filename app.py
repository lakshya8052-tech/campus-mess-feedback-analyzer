import streamlit as st
import pandas as pd

st.title("Campus Mess Food Feedback Analyzer")

# Fake dataset (same as before)
data = {
    "dish": ["Idli", "Rice", "Paneer", "Poha"],
    "rating": [4, 2, 5, 3]
}

df = pd.DataFrame(data)

st.subheader("Mess Food Ratings Data")
st.dataframe(df)

# Best and worst dish
best = df.loc[df["rating"].idxmax()]
worst = df.loc[df["rating"].idxmin()]

st.subheader("Best Dish")
st.write(best)

st.subheader("Worst Dish")
st.write(worst)

st.subheader("Ratings Visualization")
st.bar_chart(df.set_index("dish"))
