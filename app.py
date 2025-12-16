import streamlit as st
from recommender.recommend import recommend

st.set_page_config(
    page_title="SHL Assessment Recommendation",
    layout="wide"
)

st.title("SHL Assessment Recommendation System")

query = st.text_input(
    "Enter job role or skill requirements",
    placeholder="e.g. python data science entry level"
)

if st.button("Get Recommendations"):
    if query.strip() == "":
        st.warning("Please enter a query")
    else:
        results = recommend(query)

        # Remove internal columns
        display_cols = [
            col for col in results.columns
            if col.lower() not in ["combined_text"]
        ]

        results = results[display_cols].reset_index(drop=True)

        st.markdown("### Recommended Assessments")

        # Render clickable links
        for i, row in results.iterrows():
            st.markdown(f"**{i+1}. {row.get('Query', 'Assessment')}**")
            if 'Assessment_url' in row:
                st.markdown(f"[View Assessment]({row['Assessment_url']})")
            st.markdown("---")
