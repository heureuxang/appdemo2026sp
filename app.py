import streamlit as st

# Title and Header
st.title("Retail Business Dashboard")
st.header("Manager Input Section")





# Instruction

st.write("Please enter the monthly sales target and select the region.")


# Number input for sales target

sales = st.number_input("Enter Monthly Sales Target (in USD):",
                      min_value=0,
                      max_value=50000,
                      value=25)

# Dropdown for region selection

option = st.selectbox("Select Region:",
                      ["North", "South", "East","West"])
st.write(f"You selected: {option}")


# Submit button
if st.button("Submit"):
    # Display entered values
    st.write(f"The sales target entered: {sales}")
    st.write(f"The selected region: {option}")

    # Success message

st.success("Operation completed successfully!")

    # Extra message for ambitious target

