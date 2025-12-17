import streamlit as st
import pandas as pd
import re

from recommender.recommend import recommend

try:
    from rag.llm_generator import generate_explanation
    LLM_AVAILABLE = True
except:
    LLM_AVAILABLE = False

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


st.title("GenAI Assessment Recommendation System")
st.write("Enter job role or skill requirements to get relevant SHL assessments.")

query = st.text_input(
    "",
    placeholder="e.g. Entry level sales role with communication skills"
)

if st.button("Get Recommendations"):

    if not is_valid_query(query):
        st.error("Invalid input. Please enter meaningful job role or skill requirements.")

    else:
        results = recommend(query)

        if results is None or results.empty:
            st.warning("No sufficiently relevant assessments found for the given input.")

        else:
            st.success("Recommended SHL Assessments")

            for idx, row in results.iterrows():
                st.markdown("### 🔹 Assessment Recommendation")

                for col in results.columns:
                    value = row[col]

                    if isinstance(value, str) and value.startswith("http"):
                        st.markdown(f"**{col}:** [Open Assessment]({value})")
                    else:
                        st.write(f"**{col}:** {value}")

                st.markdown("---")

            if LLM_AVAILABLE:
                try:
                    assessment_names = [
                        str(v) for v in results.iloc[:, 0].tolist()
                    ]

                    explanation = generate_explanation(query, assessment_names)

                    st.markdown("## 🔍 Why these assessments?")
                    st.write(explanation)

                except Exception:
                    st.info("LLM explanation unavailable (API key not configured).")

st.caption("Powered by Retrieval-Augmented Generation on SHL Product Catalog")
