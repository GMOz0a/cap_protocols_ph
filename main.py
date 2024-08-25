import streamlit as st

#Home
home_page = st.Page("home.py", title = "Home", icon="🏚️")

#Breast 
breast_resection = st.Page("breastca_jun2024.py", title = "Breast (Carcinoma)")
phyllodes = st.Page("phyllodes_sep2022.py", title = "Phyllodes Tumor")

#Endocrine
thyroid = st.Page("thyroid_202303.py", title = "Thyroid")

#GI
ampulla = st.Page("ampulla_nov2021.py", title = "Ampulla of Vater")
colon_rectum_resection = st.Page("colon_rectum_202406.py", title = "Colon and Rectum (Resection)")
esophagus = st.Page("esophagus_jun2022.py", title = "Esophagus")
gist = st.Page("gist_sep2023.py", title = "Gist (Resection)")
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
pros_core = st.Page("proscore_sep2023.py", title = "Prostate - Core Biopsy")
pros_turp = st.Page("proturp_sep2023.py", title = "Prostate - Core Biopsy")

#Pediatric 
exgct = st.Page("exgct_sep2023.py", title = "Extragonadal Germ Cell Tumor (Resection)")

sections = {
    "Home": [home_page],
    "Breast": [breast_resection, phyllodes],
    "Endocrine": [thyroid],
    "GI": [ampulla, colon_rectum_resection, esophagus, gist, hcc, ex_panc, stomach],
    "GU": [kidney_res, pros_core, pros_turp],
    "Gynecologic": [cx_resection, endom, ovary, uterus_sarc, gtn],
    "Pediatric": [exgct]
} 
pg = st.navigation (sections)
st.set_page_config(page_title = "The Gabberbot CAP Protocols app", page_icon = ":clipboard:")
pg.run()
