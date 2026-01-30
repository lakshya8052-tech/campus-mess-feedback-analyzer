import streamlit as st
import pandas as pd

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Campus Mess Food Feedback Analyzer",
    page_icon="🍽️",
    layout="centered"
)

st.title("🍽️ Campus Mess Food Feedback Analyzer")

# -----------------------------
# Initialize session state DataFrame
# -----------------------------
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["dish", "rating"])

# -----------------------------
# Add / Update Food Rating
# -----------------------------
st.subheader("Add / Update Food Rating")

dish_name = st.text_input("Dish name")
rating_value = st.slider("Rating", 1, 5)

if st.button("Submit Rating"):
    if dish_name.strip() == "":
        st.warning("Please enter a dish name.")
    else:
        df = st.session_state.df
        if dish_name in df['dish'].values:
            # Update existing rating
            st.session_state.df.loc[df['dish'] == dish_name, 'rating'] = rating_value
            st.success(f"✅ Rating for '{dish_name}' updated to {rating_value}!")
        else:
            # Add new row
            new_row = pd.DataFrame({"dish": [dish_name], "rating": [rating_value]})
            st.session_state.df = pd.concat([df, new_row], ignore_index=True)
            st.success(f"✅ Rating for '{dish_name}' added!")

# -----------------------------
# Display all ratings
# -----------------------------
st.subheader("All Food Ratings")

if st.session_state.df.empty:
    st.info("No ratings added yet.")
else:
    # Sort by rating descending
    df_display = st.session_state.df.sort_values(by="rating", ascending=False).reset_index(drop=True)
    st.table(df_display)

    # -----------------------------
    # Key Insights
    # -----------------------------
    best = st.session_state.df.loc[st.session_state.df['rating'].idxmax()]
    worst = st.session_state.df.loc[st.session_state.df['rating'].idxmin()]
    average_rating = st.session_state.df['rating'].mean()

    st.subheader("Key Insights")
    st.write(f"🔹 Highest rated dish: **{best['dish']}** ({best['rating']}/5)")
    st.write(f"🔹 Lowest rated dish: **{worst['dish']}** ({worst['rating']}/5)")
    st.write(f"🔹 Average rating: **{average_rating:.2f}/5**")
