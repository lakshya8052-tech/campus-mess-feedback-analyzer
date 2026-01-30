import streamlit as st
import pandas as pd

# -----------------------------
# Page config (must be first)
# -----------------------------
st.set_page_config(
    page_title="Campus Mess Food Feedback Analyzer",
    page_icon="🍽️",
    layout="centered"
)

st.title("🍽️ Campus Mess Food Feedback Analyzer")

# -----------------------------
# Initialize session state for DataFrame
# -----------------------------
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["dish", "rating"])

df = st.session_state.df

# -----------------------------
# Add new rating (update if exists)
# -----------------------------
st.subheader("Add / Update Food Rating")

dish_name = st.text_input("Dish name")

# Show current rating if dish exists
if dish_name.strip() != "" and dish_name in df['dish'].values:
    current_rating = int(df.loc[df['dish'] == dish_name, 'rating'].values[0])
else:
    current_rating = 3  # default rating

rating_value = st.slider("Rating", 1, 5, value=current_rating)

if st.button("Submit Rating"):
    if dish_name.strip() == "":
        st.warning("Please enter a dish name.")
    else:
        if dish_name in df['dish'].values:
            # Update existing rating
            st.session_state.df.loc[df['dish'] == dish_name, 'rating'] = rating_value
            st.success(f"✅ Rating for '{dish_name}' updated to {rating_value}!")
        else:
            # Add new row
            new_row = pd.DataFrame({"dish": [dish_name], "rating": [rating_value]})
            st.session_state.df = pd.concat([df, new_row], ignore_index=True)
            st.success(f"🎉 Rating for '{dish_name}' added!")

# -----------------------------
# Show all ratings
# -----------------------------
st.subheader("All Food Ratings")

if df.empty:
    st.info("No ratings added yet.")
else:
    # Sort by rating descending
    st.dataframe(df.sort_values(by="rating", ascending=False).reset_index(drop=True))

    # -----------------------------
    # Key Insights
    # -----------------------------
    st.subheader("Key Insights")

    best = df.loc[df['rating'].idxmax()]
    worst = df.loc[df['rating'].idxmin()]
    avg_rating = df['rating'].mean()

    st.write(f"🔹 Highest rated dish: **{best['dish']}** ({best['rating']}/5)")
    st.write(f"🔹 Lowest rated dish: **{worst['dish']}** ({worst['rating']}/5)")
    st.write(f"🔹 Average rating: **{avg_rating:.2f}/5**")
