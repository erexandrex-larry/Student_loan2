import streamlit as st


st.title("Student Loan Application Form")


first_name = st.text_input(
        label ="First name",
        placeholder = "Enter your first name",
        )


middle_name = st.text_input(
        label ="Middle name",
        placeholder = "Enter your middle name",
        )


last_name = st.text_input(
        label ="Last name",
        placeholder = "Enter your last name",
        )


email_address = st.text_input(
        label ="Email address",
        placeholder = "Enter your email address",
        )


loan_amount = st.text_input(
        label ="Loan Amount",
        placeholder = "Enter your loan amount",
        )




name_of_institution = st.text_input(
        label ="Name of institution",
        placeholder = "Enter name of your institution",
        )



residential_address = st.text_input(
        label ="Residential Address",
        placeholder = "Enter your residential address",
        )


guarantor_name = st.text_input(
        label ="Guarantor Name",
        placeholder = "Enter your guarantor name",
        )

repayment_method = [
    "Mobile Money",
    "Bank Transfer",
    "Cash Payment"
    "Wire transfer",
]

indicate_repayment_method = st.selectbox(
        label ="Repayment Method",
        options = repayment_method,
        placeholder = "Select your repayment method",
        )



cities_in_ghana = [
    "Accra",
    "Kumasi",
    "Tamale",
    "Takoradi",
    "Ashiaman",
    "Tema",
    "Cape Coast",
    "Obuasi",
    "Sunyani",
    "Sekondi-Takoradi",
]

city = st.selectbox(
        label ="City",
        options = cities_in_ghana,
        placeholder = "Select your city",
        )

button = st.button(
        label = "Submit form",
        key="Submit_button",
)