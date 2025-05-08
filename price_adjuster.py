import streamlit as st
import pandas as pd

# Function to load vendor catalog and apply price adjustment
def adjust_prices(catalog, percentage_increase=25):
    # Ensure price column exists
    if 'Price' not in catalog.columns:
        raise ValueError("The catalog must have a 'Price' column.")
    
    # Calculate the new prices
    catalog['New Price'] = catalog['Price'] * (1 + percentage_increase / 100)
    
    return catalog

# Streamlit App UI
st.title("Vendor Catalog Price Adjuster")
st.markdown("Upload your vendor catalog (CSV file) to automatically adjust the prices by 25%.")

# File uploader for vendor catalog
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        # Read the uploaded CSV file
        catalog = pd.read_csv(uploaded_file)
        
        # Display the original catalog
        st.subheader("Original Catalog")
        st.write(catalog)
        
        # Adjust prices
        adjusted_catalog = adjust_prices(catalog)
        
        # Display the updated catalog
        st.subheader("Updated Catalog (Price +25%)")
        st.write(adjusted_catalog)
        
        # Provide download link for updated catalog
        st.download_button(
            label="Download Updated Catalog",
            data=adjusted_catalog.to_csv(index=False),
            file_name="updated_vendor_catalog.csv",
            mime="text/csv"
        )
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
