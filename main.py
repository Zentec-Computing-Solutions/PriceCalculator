
import streamlit as st

st.set_page_config(page_title="Zentec Calculator",
                   page_icon="🧮", layout="centered")

st.markdown("""
<h1 style='text-align: center; color: #1f77b4;'>🧮 Zentec Calculator</h1>
<h3 style='text-align: center; color: #00bfff;'>Created by Caleb</h3>
<hr>
""", unsafe_allow_html=True)


inputStr = st.number_input("Input Value...", step=1, min_value=0, value=None)
result = None
error = None

if inputStr:
    try:
        inputInt = float(inputStr)
        if inputInt == 0:
            error = "An expected error occurred, stop trying to multiply by zero."
        elif inputInt < 10:
            result = round(inputInt * 2, 2)
        elif 9.99 < inputInt < 15:
            result = round(inputInt * 1.9, 2)
        elif 14.99 < inputInt < 20:
            result = round(inputInt * 1.8, 2)
        elif 19.99 < inputInt < 25:
            result = round(inputInt * 1.75, 2)
        elif 24.99 < inputInt < 30:
            result = round(inputInt * 1.7, 2)
        elif 29.99 < inputInt < 35:
            result = round(inputInt * 1.65, 2)
        elif 34.99 < inputInt < 40:
            result = round(inputInt * 1.6, 2)
        elif 39.99 < inputInt < 45:
            result = round(inputInt * 1.55, 2)
        elif 44.99 < inputInt < 60:
            result = round(inputInt * 1.5, 2)
        elif 59.99 < inputInt < 70:
            result = round(inputInt * 1.48, 2)
        elif 69.99 < inputInt < 80:
            result = round(inputInt * 1.47, 2)
        elif 79.99 < inputInt < 90:
            result = round(inputInt * 1.46, 2)
        elif 89.99 < inputInt < 100:
            result = round(inputInt * 1.45, 2)
        elif 99.99 < inputInt < 110:
            result = round(inputInt * 1.44, 2)
        elif 109.99 < inputInt < 120:
            result = round(inputInt * 1.43, 2)
        elif 119.99 < inputInt < 130:
            result = round(inputInt * 1.42, 2)
        elif 129.99 < inputInt < 140:
            result = round(inputInt * 1.41, 2)
        elif 139.99 < inputInt < 150:
            result = round(inputInt * 1.4, 2)
        elif 149.99 < inputInt < 160:
            result = round(inputInt * 1.39, 2)
        elif 159.99 < inputInt < 170:
            result = round(inputInt * 1.38, 2)
        elif 169.99 < inputInt < 180:
            result = round(inputInt * 1.37, 2)
        elif 179.99 < inputInt < 190:
            result = round(inputInt * 1.36, 2)
        elif 189.99 < inputInt < 200:
            result = round(inputInt * 1.35, 2)
        elif 199.99 < inputInt < 225:
            result = round(inputInt * 1.345, 2)
        elif 224.99 < inputInt < 250:
            result = round(inputInt * 1.34, 2)
        elif 249.99 < inputInt < 300:
            result = round(inputInt * 1.335, 2)
        elif 299.99 < inputInt < 375:
            result = round(inputInt * 1.33, 2)
        elif 374.99 < inputInt < 475:
            result = round(inputInt * 1.325, 2)
        elif 474.99 < inputInt < 550:
            result = round(inputInt * 1.32, 2)
        elif 549.99 < inputInt < 650:
            result = round(inputInt * 1.315, 2)
        elif 649.99 < inputInt < 750:
            result = round(inputInt * 1.31, 2)
        elif 749.99 < inputInt < 850:
            result = round(inputInt * 1.305, 2)
        elif 849.99 < inputInt < 1000:
            result = round(inputInt * 1.3, 2)
        elif 999.99 < inputInt < 1100:
            result = round(inputInt * 1.295, 2)
        elif 1099.99 < inputInt < 1200:
            result = round(inputInt * 1.29, 2)
        elif 1199.99 < inputInt < 1300:
            result = round(inputInt * 1.285, 2)
        elif 1299.99 < inputInt < 1400:
            result = round(inputInt * 1.28, 2)
        elif 1399.99 < inputInt < 1500:
            result = round(inputInt * 1.275, 2)
        elif 1499.99 < inputInt < 1600:
            result = round(inputInt * 1.27, 2)
        elif 1599.99 < inputInt < 1700:
            result = round(inputInt * 1.265, 2)
        elif 1699.99 < inputInt < 1800:
            result = round(inputInt * 1.26, 2)
        elif 1799.99 < inputInt < 1900:
            result = round(inputInt * 1.225, 2)
        elif 1899.99 < inputInt < 2000:
            result = round(inputInt * 1.25, 2)
        elif inputInt > 1999.99:
            result = round(inputInt * 1.2, 2)
    except ValueError:
        error = "Error: Please enter a valid number."

if result is not None:
    st.success(str(result))

elif error:
    st.error(error)
