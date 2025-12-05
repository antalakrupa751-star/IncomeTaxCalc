import streamlit as st
st.write("AS PER OLD REGIME")
def calculate_tax(income):
    tax = 0.0  # must not be a number, not tuple
    if income <= 300000:
        tax = 0

    elif income <= 600000:
        tax = (income - 300000) * 0.05

    elif income <= 900000:
        tax = (300000 * 0.05) + (income - 600000) * 0.10

    elif income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.10) + (income - 900000) * 0.15

    elif income <= 1500000:
        tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (income - 1200000) * 0.20

    else:
        tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (income - 1500000) * 0.30

    # Rebate under section 87A
    if income <= 700000:
        tax = 0

    # Add 4% Health and Education Cess
    cess = tax * 0.04
    total_tax = tax + cess

    return tax, cess, total_tax


# Main Program
income = float(st.number_input("Enter your annual income (₹): "))

basic_tax, cess_amount, total_payable = calculate_tax(income)
        
st.write("\nTotal Income Tax Payable for AY 2025-26")
st.write("-------------------------------------------")
st.write(f"Taxable income           :₹{income:,.2f}")
st.write(f"Basic Income Tax         :₹{basic_tax:,.2f}")
st.write(f"Health and Education Cess:₹{cess_amount:,.2f}")
st.write(f"Total Tax Payable        : ₹{total_payable:,.2f}")
