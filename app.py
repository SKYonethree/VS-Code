# Import all necessary packages
import streamlit as st

# Write a function to calculate EMI
def loanCalc(P, N, R):
    """
    This function takes Principal , Number of Years
    and Rate of Interest and calculates loan details
    """

    # Convert years to month and rate of interest to %per month
    n = N*12
    r = R/1200
    # Calculate EMI
    x = (1+r)**n
    emi = P*r*x/(x-1)
    # Calculate total amount
    amt = emi*n
    # Calculate interest
    I = amt - P
    # Calculate percent interest
    perI= (I/amt)*100
    return emi, amt, I, perI
    
# Write the streamlit app
def application():

    # Header of the application
    st.set_page_config(page_title="Loan Calculator - SKY")
    # Show application  title
    st.title("Loan Calculator - SKY")
    # Add the subheading
    st.subheader("Please provide loan details below")
    # Get princupal, period and rate of interest
    P = st.number_input("Principal (INR) : ",min_value=0.00, step=0.01)
    N = st.number_input("Number of Years : ",min_value=0.00, step=0.01)
    R = st.number_input("Rate of Interest  in %p.a. :", min_value=0.00, max_value=100.00, step=0.01)
    # Add  a button to perform calculations
    btn = st.button("Calculate")
    # After button is clicked
    if btn:
        emi, amt, I, perI = loanCalc(P, N, R)
        st.subheader("Loan Details Calculated:")
        st.write(f"**EMI** : {emi:.0f} INR")
        st.write(f"**Interest** : {I:.0f} INR")
        st.write(f"**Total Amount** : {amt:.0f} INR")
        st.write(f"**Percentage Interest** : {perI:.2f} %")

# Main application below
if __name__ == "__main__":
    application()
