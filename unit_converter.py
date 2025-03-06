import streamlit as st

st.title("Unit Converter App")
st.markdown("##### converts Length, Weight And Time Instantiy")
st.write("Welcome! select the category enter a value and get the converts result in real-time")

category = st.selectbox("choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometer to Mile":
            return value * 0.621371
        elif unit == "Mile to Kilometer":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilometer to pound":
            return value * 2.20462
        elif unit == "Pound to kilometer":
            return value / 2.20462
    elif category == "Time":
        if unit == "Second to minute":
            return value / 60
        elif unit == "Minute to second":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Day to hours":
            return value / 24
        elif unit == "Hours to day":
            return value * 24

if category == "Length":
    unit = st.selectbox ("Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
       unit = st .selectbox("Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st .selectbox("Select Conversion", ["Second to minutes", "Minutes to second", "Minutes to hours", "Hours to minutse", "Day to hours", "Hours to day"])

value = st.number_input("Enter The Value to converts")

result = convert_units(category, value, unit)
if st.button("Convert"):
    st.success(f"The result is {result:2f}")
