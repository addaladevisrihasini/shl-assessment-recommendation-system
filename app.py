import streamlit as st
import pandas as pd
import re

from recommender.recommend import recommend

st.set_page_config(
    page_title="SHL Assessment Recommendation System",
    layout="wide"
)

def is_valid_query(text):
    if not text or len(text.strip()) < 6:
        return False


    if not re.search(r"[a-zA-Z]{3,}", text):
        return False


    if len(set(text.lower())) <= 4:
        return False

    return True

st.title("SHL Assessment Recommendation System")
st.write("Enter job role or skill requirements")

query = st.text_input(
    "",
    placeholder="e.g. Entry level sales role, communication skills, 0–2 years experience"
)

if st.button("Get Recommendations"):

    if not is_valid_query(query):
        st.error("Invalid input. Please enter meaningful job role or skill requirements.")

    else:
        results = recommend(query)

        if results is None or results.empty:
            st.warning("No sufficiently relevant assessments found for the given input.")

        else:
            st.success("Recommended Assessments")

            url_cols = [c for c in results.columns if "url" in c.lower()]

            for idx, row in results.iterrows():
                st.markdown("### 🔹 Assessment Recommendation")

                for col in results.columns:
                    if col in url_cols:
                        st.markdown(f"**{col}:** [Open Assessment]({row[col]})")
                    else:
                        st.write(f"**{col}:** {row[col]}")

                st.markdown("---")

st.caption("Powered by TF-IDF similarity on SHL product catalog")
