import streamlit as st

#Home
home_page = st.Page("home.py", title = "Home", icon="🏚️")

#Breast 
breast_resection = st.Page("breastca_jun2024.py", title = "Breast (Carcinoma)")
phyllodes = st.Page("phyllodes_sep2022.py", title = "Phyllodes Tumor")

#Endocrine
thyroid = st.Page("thyroid_202303.py", title = "Thyroid")
adrenal = st.Page("adrenal_mar2023.py", title = "Adrenal Gland")

#GI
ampulla = st.Page("ampulla_nov2021.py", title = "Ampulla of Vater")
anus = st.Page("anus_sep2023.py", title = "Anus")
appendix =  st.Page("appendix_dec2022.py", title = "Appendix") 
colon_rectum_resection = st.Page("colon_rectum_202406.py", title = "Colon and Rectum (Resection)")
dehb = st.Page("dehb_jun2021.py", title = "Distal Extrahepatic Bile Ducts")
esophagus = st.Page("esophagus_jun2022.py", title = "Esophagus")
gallbladder = st.Page("gb_jun2021.py", title = "Gallbladder")
gist = st.Page("gist_sep2023.py", title = "GIST (Resection)")
hcc = st.Page("HCC_Jun2022.py", title = "Hepatocellular Carcinoma")
ihb = st.Page("ihb_jun2021.py", title = "Intrahepatic Bile Ducts")
phb = st.Page("phb_jun2021.py", title = "Perihilar Bile Ducts")
ex_panc = st.Page("expan_nov2021.py", title = "Pancreas (Exocrine)")
stomach = st.Page("stomach_mar2023.py", title = "Stomach")

#Gynecologic
cx_bx = st.Page("cxbx_mar2023.py", title = "Cervix (Biopsy)")
cx_resection = st.Page("cx_april2023.py", title = "Cervix (Resection)")
endom = st.Page("endom_2023.py", title = "Endometrium")
ovary = st.Page("ovary_jun2024.py", title = "Ovary")
uterus_sarc = st.Page("uterus_sarc_mar2022.py", title = "Uterine Sarcoma")
vulva = st.Page("vulva_jun2024.py", title = "Vulva")
gtn = st.Page("gtn_nov2021.py", title = "Trophoblastic Tumors")

# GU
bladder = st.Page("bladder_sep2023.py", title = "Bladder (Resection)")
kidney_res = st.Page("kidney_jun2024.py", title = "Kidney (Resection)")
pros_core = st.Page("proscore_sep2023.py", title = "Prostate - Core Biopsy")
pros_resection = st.Page("prostateres_sep2023.py", title = "Prostate - Resection")
pros_turp = st.Page("proturp_sep2023.py", title = "Prostate - TURP")
testis = st.Page("testis_sep2023.py", title = "Testis")

# Head and Neck
larynx = st.Page("larynx_jun2023.py", title = "Larynx")
oral = st.Page("oral_jun2023.py", title = "Oral Cavity")
salivary = st.Page("salivary_jun2023.py", title = "Salivary Gland")

#Pediatric 
exgct = st.Page("exgct_sep2023.py", title = "Extragonadal Germ Cell Tumor (Resection)")

#Thoracic
lung = st.Page("lung_sep2022.py", title = "Lung (Resection)")
thymus = st.Page("thymus_jun2021.py", title = "Thymus (June 2021)")
meso = st.Page("meso_jun2021.py", title = "Pleural Mesothelioma (June 2021)")

sections = {
    "Home": [home_page],
    "Breast": [breast_resection, phyllodes],
    "Endocrine": [thyroid, adrenal],
    "GI": [ampulla, anus, appendix, colon_rectum_resection, dehb,
           esophagus, gallbladder, gist, hcc,ihb, ex_panc, phb, stomach],
    "GU": [bladder, kidney_res, pros_core, pros_resection, pros_turp],
    "Gynecologic": [cx_bx, cx_resection, endom, ovary, uterus_sarc, vulva, gtn],
    "Head and Neck": [larynx, oral, salivary],
    "Pediatric": [exgct],
    "Thorax": [lung, thymus, meso]
} 
pg = st.navigation (sections)
st.set_page_config(page_title = "The Gabberbot CAP Protocols app", page_icon = ":clipboard:")
pg.run()
