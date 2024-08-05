import streamlit as st

breast_resection = st.Page("breast_202406.py", title = "Breast (Carcinoma)")
colon_rectum_resection = st.Page("colon_rectum_202406.py", title = "Colon and Rectum (Resection)")
thyroid = st.Page("thyroid_202303.py", title = "Thyroid")

sections = {
    "Breast": breast_resection,
    "Endocrine": thyroid,
    "GI": colon_rectum_resection,
}

pg = st.navigation (sections)
st.set_page_config(page_title = "Cancer  Reporting Protocols", page_icon = ":clipboard:")
pg.run()
