import streamlit as st
import pickle
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import time
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://online.stat.psu.edu/stat462/sites/onlinecourses.science.psu.edu.stat462/files/02simple/temps/index.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

# Apply background image
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the pickled data
df = pickle.load(open('df.pkl', 'rb'))
l = pickle.load(open('l.pkl', 'rb'))
m = pickle.load(open('m.pkl', 'rb'))

st.title('Linear Regression Model')

# Input for the year
year_input = st.text_area("Enter year in the text area")

# Button to generate the prediction
if st.button("Click OK"):
    try:
        year = float(year_input)
        st.write(f"Year: {year}")

        # Predict the price for the input year
        x = float(l[0])
        c = float(l[1])
        price_prediction = year * x + c

        # Load and display the scatter plot image
        image = Image.open('scatter_plot.png')
        st.image(image, caption='Scatter Plot', use_column_width=True)

        # Display the prediction
        st.header(f"Predicted price for the year {year}: {price_prediction}")

        # Ask if the user wants to see the line plot


    except ValueError:
        st.write("Please enter a valid year.")
with st.expander("Do you want to see the line plot?"):

            select_val = st.selectbox("Select an option", ["yes", "no"])

            if 'yes' in select_val:
                line_image = Image.open('linefig.png')
                st.image(line_image, caption='Line Plot', use_column_width=True)
                
