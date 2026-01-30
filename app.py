st.set_page_config(
    page_title="Campus Mess Food Feedback Analyzer",
    page_icon="🍽️",
    layout="centered"
)

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
st.subheader("Key Insights")

st.write(f"🔹 Highest rated dish: **{best['dish']}** ({best['rating']}/5)")
st.write(f"🔹 Lowest rated dish: **{worst['dish']}** ({worst['rating']}/5)")


st.subheader("Add New Food Rating")

dish_name = st.text_input("Dish name")
rating_value = st.slider("Rating", 1, 5)

if st.button("Submit Rating"):
    new_row = pd.DataFrame(
        {"dish": [dish_name], "rating": [rating_value]}
    )
    df = pd.concat([df, new_row], ignore_index=True)
    st.success("Rating added!")
