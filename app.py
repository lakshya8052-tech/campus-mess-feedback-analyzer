import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Campus Mess Food Feedback Analyzer",
    page_icon="🍽️",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("Campus Mess Food Feedback Analyzer")

# -----------------------------
# Initialize session state
# -----------------------------
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({
        "dish": ["Idli", "Rice", "Paneer", "Poha"],
        "rating": [4, 2, 5, 3]
    })


# -----------------------------
# Display current data
# -----------------------------
st.subheader("Mess Food Ratings Data")

# Add this line before your st.dataframe(st.session_state.df) call
def get_sentiment(r):
    return "🟢 Positive" if r >= 4 else "🟡 Neutral" if r == 3 else "🔴 Negative"

df_display = st.session_state.df.copy()
df_display["Sentiment"] = df_display["rating"].apply(get_sentiment)
st.dataframe(df_display) # Use this copy for the display

st.dataframe(st.session_state.df)

# -----------------------------
# Key Insights
# -----------------------------
st.subheader("Key Insights")

df = st.session_state.df
if not df.empty:
    best = df.loc[df["rating"].idxmax()]
    worst = df.loc[df["rating"].idxmin()]

    st.write(f"🔹 Highest rated dish: **{best['dish']}** ({best['rating']}/5)")
    st.write(f"🔹 Lowest rated dish: **{worst['dish']}** ({worst['rating']}/5)")
else:
    st.write("No ratings yet.")



# -----------------------------
# Add new rating (update if exists)
# -----------------------------
st.subheader("Add New Food Rating")

dish_name = st.text_input("Dish name")
rating_value = st.slider("Rating", 1, 5)

if st.button("Submit Rating"):
    if dish_name.strip() == "":
        st.warning("Please enter a dish name.")
    else:
        # Check if dish already exists
        df = st.session_state.df
        if dish_name in df['dish'].values:
            # Update existing rating
            st.session_state.df.loc[df['dish'] == dish_name, 'rating'] = rating_value
            st.success(f"Rating for '{dish_name}' updated to {rating_value}!")
        else:
            # Add new row
            new_row = pd.DataFrame({"dish": [dish_name], "rating": [rating_value]})
            st.session_state.df = pd.concat([df, new_row], ignore_index=True)
            st.success(f"Rating for '{dish_name}' added!")


# -----------------------------
# Management Action Alerts
# -----------------------------
st.subheader("Management Action Alerts")
low_rated = df[df["rating"] <= 2]

if not low_rated.empty:
    for _, row in low_rated.iterrows():
        st.error(f"Action Required: Improve or Replace **{row['dish']}** (Critical Rating: {row['rating']})")
else:
    st.success("✅ All current dishes are performing above critical levels.")

# -----------------------------
# Ratings Visualization
# -----------------------------
st.subheader("Ratings Visualization")
st.bar_chart(df.set_index("dish"))
