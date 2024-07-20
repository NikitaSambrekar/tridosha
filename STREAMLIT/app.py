import streamlit as st


# Function to provide diet plans based on dosha type, age, and weight
def get_diet_plan(dosha, age):
    diet_plans = {
        "Vata": {
            "child": "Warm, nourishing foods like soups and stews, root vegetables, and whole grains.",
            "adult": "Cooked vegetables, warming spices, dairy, and well-cooked grains.",
            "elderly": "Warm, soft foods with moderate oil, easily digestible grains, and cooked fruits."
        },
        "Pitta": {
            "child": "Cooling foods like cucumber, melon, and dairy products. Avoid spicy foods.",
            "adult": "Fresh fruits and vegetables, especially bitter greens, and cooling herbs.",
            "elderly": "Cool, light foods, avoiding too much salt and spices. Fresh juices and salads."
        },
        "Kapha": {
            "child": "Light, warm foods like steamed vegetables and lean proteins. Avoid dairy and heavy foods.",
            "adult": "Spicy, light, and dry foods. Include lots of vegetables and legumes.",
            "elderly": "Warm, light foods with spices like ginger and black pepper. Avoid heavy and oily foods."
        }
    }
    
    if age < 18:
        age_group = "child"
    elif 18 <= age <= 60:
        age_group = "adult"
    else:
        age_group = "elderly"
        
    return diet_plans[dosha][age_group]

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
    diet_plan = get_diet_plan(dosha, age)
    st.write("### Recommended Diet Plan:")
    st.write(diet_plan)

    # Provide additional tips and suggestions
    st.write("#### Additional Tips:")
    if dosha == "Vata":
        st.write("Stay warm and hydrated. Incorporate regular meals and avoid cold and raw foods.")
    elif dosha == "Pitta":
        st.write("Stay cool and avoid overly spicy and oily foods. Incorporate cooling herbs and fresh fruits.")
    elif dosha == "Kapha":
        st.write("Stay active and incorporate spices into your diet. Avoid heavy and oily foods.")

# Footer
    st.write("Thank you for providing your information. Based on the provided details, please follow the recommended diet plan for better health.")

