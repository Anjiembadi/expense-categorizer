import streamlit as st
from main import categorize_expense

st.set_page_config(page_title="Expense Categorizer", page_icon="💸")
st.title("💸 Expense Categorizer")
st.write("Enter any expense description to classify it automatically.")

description = st.text_input("Expense Description", placeholder="e.g. paid electricity bill")

if st.button("Categorize"):
    if description.strip():
        with st.spinner("Analyzing..."):
            result = categorize_expense(description)
        st.success("Expense categorized successfully!")
        col1, col2 = st.columns(2)
        col1.metric("Category", result.expense_category)
        col2.metric("Type", result.expense_type)
        st.info(f"📝 {result.confidence_note}")
    else:
        st.warning("Please enter a description.")
