import streamlit as st

def main():

    st.title("Hello! I am your meal plan assistant")

    diet_pref = st.selectbox("Diet Preference", ["Egg-etarian", "Non-vegetarian", "Vegetarian"])
    no_of_ppl = st.selectbox("Count of people eating every meal", [1, 2, 3, 4, 5, 6, 7])
    cuisine_pref = st.selectbox("Cuisine Preference", ["East Indian", "North Indian", "South Indian", "West Indian"])
    day_type = st.selectbox("Type of day", ["Breakfast-Lunch-Dinner", "Brunch-Snack-Dinner"])

    if st.button("Submit"):
        selections = {"Diet Preference": diet_pref, "PPl Count": no_of_ppl, "Cuisine Preference": cuisine_pref, "Type of day": day_type}
        st.write("Selections:", selections)


if __name__ == "__main__":
    main()
