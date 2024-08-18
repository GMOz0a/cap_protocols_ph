import streamlit as st

#Home
home_page = st.Page("home.py", title = "Home", icon="🏚️")

#Breast 
breast_resection = st.Page("breast_202406.py", title = "Breast (Carcinoma)")
phyllodes = st.Page("phyllodes_sep2022.py", title = "Phyllodes Tumor")

#Endocrine
thyroid = st.Page("thyroid_202303.py", title = "Thyroid")

#GI
colon_rectum_resection = st.Page("colon_rectum_202406.py", title = "Colon and Rectum (Resection)")
esophagus = st.Page("esophagus_jun2022.py", title = "Esophagus")
hcc = st.Page("HCC_Jun2022.py", title = "Hepatocellular Carcinoma")
ex_panc = st.Page("expan_nov2021.py", title = "Pancreas (Exocrine)")
stomach = st.Page("stomach_mar2023.py", title = "Stomach")

#Gynecologic
cx_resection = st.Page("cx_april2023.py", title = "Cervix (Resection)")
endom = st.Page("endom_2023.py", title = "Endometrium")
ovary = st.Page("ovary_jun2024.py", title = "Ovary")
uterus_sarc = st.Page("uterus_sarc_mar2022.py", title = "Uterine Sarcoma")
gtn = st.Page("gtn_nov2021.py", title = "Trophoblastic Tumors")

# GU
kidney_res = st.Page("kidney_jun2024.py", title = "Kidney (Resection)")

#Pediatric 
exgct = st.Page("exgct_sep2023.py", title = "Extragonadal Germ Cell Tumor (Resection)")

sections = {
    "Home": [home_page],
    "Breast": [breast_resection, phyllodes],
    "Endocrine": [thyroid],
    "GI": [colon_rectum_resection, esophagus, hcc, ex_panc, stomach],
    "GU": [kidney_res],
    "Gynecologic": [cx_resection, endom, ovary, uterus_sarc, gtn],
    "Pediatric": [exgct]
} 
pg = st.navigation (sections)
st.set_page_config(page_title = "The Gabberbot CAP Protocols app", page_icon = ":clipboard:")
pg.run()
