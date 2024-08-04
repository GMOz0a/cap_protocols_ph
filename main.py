import streamlit as st

breast_resection = st.Page("breast_202406.py", title = "Breast (Carcinoma)")
colon_rectum_resection = st.Page("colon_rectum_202406.py", title = "Colon and Rectum (Resection)")

pg = st.navigation ([breast_resection, colon_rectum_resection])
st.set_page_config(page_title = "Cancer  Reporting Protocols", page_icon = ":clipboard:")
pg.run()