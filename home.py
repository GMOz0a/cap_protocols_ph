import streamlit as st

st.header(":robot_face: Welcome to the CAP synoptic protocol app!")
st.subheader(":teacher: General Instructions")

st.markdown("""
            1. Choose a protocol from the sidebar.
            2. Each section generates a single line in the report. Any section left blank will not be included in the report. 
            3. For **"other tissue/organs"** and **"lymph nodes"** involved by tumor: if you choose to specify the status of each specimen with their corresponding labels, please choose the option which has the phrase **"Specify individually"**.
            4. Do not forget to press "Enter" every time you type an entry into any text field, for it to be saved/cached. A preview will be shown at the bottom of each section which confirms that your input has been included into the final report. 
            5. Press **"Add to Report"** to include the line into the final report.
            6. Press **"Remove from Report"** to remove the line from the final report.
            7. The final report can be found at the end of all of the sections. 
            8. Do not forget to click **Copy to Clipboard** icon and paste your final report onto a different text file. 
""")
st.info("Will try to include one protocol every 2 to 3 days or one entire section each week so stay tuned :v:. For any feedback, or any bug you may encounter, please let me know! ")

st.divider()
st.markdown("### :black_nib: Updates")
st.markdown("""
    * **2024/09/09**: Added Larynx, Salivary Gland, Oral Cavity, Vulva, Gallbladder, Adrenal Gland, Prostate (Resection), and Testis Protocols
    * **2024/09/03**: Added Bladder (Resection), Cervix (Biopsy), Anus, and Appendix Protocols.
    * **2024/08/25**: Revised Breast (Carcinoma) Protocol.
    * **2024/08/24**: Added GIST (Resection), Ampulla of Vater, Prostate (Core), and Prostate (TURP) Protocols.
    * **2024/08/18**: Added Kidney, Phyllodes, and Extragonadal Germ Cell Tumor Protocols.
    * **2024/08/15**: Added Esophagus, Stomach, HCC and Exocrine Pancreas Protocols; Revised Breast (Resection) protocol.
    * **2024/08/11**: Launched the 'Gynecologic' protocols.
    * **2024/08/05**: Included the Thyroid protocol.
    * **2024/08/04**: Launched the CAP synoptic protocols: Breast and Colon/Rectum.
""")
