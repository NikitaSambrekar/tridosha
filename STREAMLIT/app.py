import streamlit as st
from PIL import Image




# Function to style the app



# Title of the app
st.title("🌿 Tridosha Imbalance Assessment and Diet Plan 🌿")

# Header
st.header("Please enter your details")

# Input widget: Text input for name
name = st.text_input("Name")

# Input widget: Number input for age
age = st.number_input("Age", min_value=0, max_value=120, step=1)

# Input widget: Number input for weight
weight = st.number_input("Weight (kg)", min_value=0, max_value=200, step=1)

# Input widget: Radio button for gender
gender = st.radio("Gender", ("Male", "Female", "Other"))

# Multiselect widget for symptoms
symptoms = st.multiselect(
    "Symptoms",
    [
        "Headache",
        "Fatigue",
        "Digestive issues",
        "Insomnia",
        "Anxiety",
        "Joint pain",
        "Skin problems",
        "Respiratory issues",
        "Other"
    ]
)

# Selectbox for dosha type
dosha = st.selectbox(
    "Dosha Type",
    ("Vata", "Pitta", "Kapha")
)

# Text area for additional details
additional_details = st.text_area("Additional Details (Optional)")

# Button widget
if st.button("Submit"):
    st.write("### Summary of your information:")
    st.write(f"*Name:* {name}")
    st.write(f"*Age:* {age}")
    st.write(f"*Weight:* {weight} kg")
    st.write(f"*Gender:* {gender}")
    st.write(f"*Symptoms:* {', '.join(symptoms)}")
    st.write(f"*Dosha Type:* {dosha}")
    if additional_details:
        st.write(f"*Additional Details:* {additional_details}")
    else:
        st.write("No additional details provided.")
    
    # Display diet plan
    
    st.write("### Recommended Diet Plan:")
   

    # Provide additional tips and suggestions
    st.write("#### Additional Tips:")
    
# Footer
st.write("Thank you for providing your information. Based on the provided details, please follow the recommended diet plan for better health.")

