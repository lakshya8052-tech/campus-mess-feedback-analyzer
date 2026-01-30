import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Campus Mess Food Feedback Analyzer")

data = {
    "dish": ["Idli", "Rice", "Paneer", "Poha"],
    "rating": [4, 2, 5, 3]
}

df = pd.DataFrame(data)

st.subheader("Mess Food Ratings Data")
st.dataframe(df)

best = df.loc[df["rating"].idxmax()]
worst = df.loc[df["rating"].idxmin()]

st.subheader("Best Dish")
st.write(best)

st.subheader("Worst Dish")
st.write(worst)

st.subheader("Ratings Visualization")

fig, ax = plt.subplots()
ax.bar(df["dish"], df["rating"])
ax.set_xlabel("Dish")
ax.set_ylabel("Rating")
ax.set_title("Mess Food Ratings")
st.pyplot(fig)
