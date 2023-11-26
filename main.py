import streamlit as st
import pandas as pd
from search_engine import *
from file_parsers import *

pdf_data = parse_pdf_directory('documents/')
reverse_index = build_reverse_index(pdf_data)

# Streamlit App
st.title("PDF Search Engine")

# User Input: Search Query
user_query = st.text_input("Enter your search query:")

# Button to Trigger Search
if st.button("Search"):
    if user_query:
        # Perform search
        search_results = search(user_query, reverse_index)

        # Display Results
        st.subheader("Matching Documents:")
        if search_results:
            for filename in search_results:
                st.write(f"- {filename}")
        else:
            st.write("No matching documents found.")
    else:
        st.warning("Please enter a search query.")