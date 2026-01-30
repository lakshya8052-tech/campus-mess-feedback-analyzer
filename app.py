import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Campus Mess Food Feedback Analyzer", page_icon="🍽️", layout="centered")

st.title("Campus Mess Food Feedback Analyzer")

# 2. Initialize Data
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({
        "dish": ["Idli", "Rice", "Paneer", "Poha"],
        "rating": [4, 2, 5, 3]
    })

df = st.session_state.df

# 3. Display Current Data & Insights (Show these FIRST)
st.subheader("Mess Food Ratings Data")
st.dataframe(df)

st.subheader("Key Insights")
if not df.empty:
    best = df.loc[df["rating"].idxmax()]
    worst = df.loc[df["rating"].idxmin()]
    st.write(f"🔹 Highest rated dish: **{best['dish']}** ({best['rating']}/5)")
    st.write(f"🔹 Lowest rated dish: **{worst['dish']}** ({worst['rating']}/5)")

# 4. Visualization
st.subheader("Ratings Visualization")
st.bar_chart(df.set_index("dish"))

# 5. Add New Food Rating (Moved to the BOTTOM)
st.divider() # Adds a clean visual line
st.subheader("Submit New Feedback")
dish_name = st.text_input("Dish name")
rating_value = st.slider("Rating", 1, 5)

if st.button("Submit Rating"):
    if dish_name.strip() != "":
        if dish_name in st.session_state.df['dish'].values:
            st.session_state.df.loc[st.session_state.df['dish'] == dish_name, 'rating'] = rating_value
        else:
            new_row = pd.DataFrame({"dish": [dish_name], "rating": [rating_value]})
            st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
        st.rerun() # Refresh to show new data at the top



# -----------------------------
# Management Action Alerts
# -----------------------------
st.subheader("⚠️ Management Action Alerts")
low_rated = df[df["rating"] <= 2]

if not low_rated.empty:
    for _, row in low_rated.iterrows():
        st.error(f"Action Required: Improve or Replace **{row['dish']}** (Critical Rating: {row['rating']})")
else:
    st.success("✅ All current dishes are performing above critical levels.")
