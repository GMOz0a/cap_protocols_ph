import streamlit as st
import pickle
from st_copy_to_clipboard import st_copy_to_clipboard

st.header("CAP Synoptic Reporting: Thyroid (March 2023)")
st.subheader(":eyeglasses: Instructions:")
st.markdown("""
        1. Input all lines you wish to include into the report and then click the **\"Add to Report\"** button. **If a text input field is required in one of the sections, please press "Enter" first after typing in your entry and before clicking the "Add Report" button. Otherwise, it will not be included into the line.** Any line/section left blank will _**not**_ be seen in the final report. *There's no need to worry about the upper/lower case and indentations - this will be reflected in the final report.* Additional notes for each section are included at the end of each section/expandable window.
        2. If you wish to remove a line, click the **\"Remove from Report\"** button. 
        3. A preview of the line will be updated at each section. The text for the final report which can be seen at the end of the page will be updated as you go add/remove each line.
        4. The final report will be previewed at the end of all sections. Click the checkbox :clipboard: at the bottom of the page to copy the entire report to your clipboard, and paste it to your chosen text platform. **_Reminder: this app does not save any of your written reports._** So once you've finished with a report, do not forget to copy it and paste it onto a text file somewhere else.
        6. If you want to start over with a new outline, click the **\"Clear Report\"** button.
         """)

with open("data/thyroid_2023.pkl", 'rb') as fp:
    data = pickle.load(fp)

if "protocol_content_thyroid" not in st.session_state:
    st.session_state.protocol_content_thyroid = {k:v for k, v in zip(data.keys(), [""] * len(data))}
    st.session_state.protocol_content_thyroid["Additional Findings"] = "" 

st.divider()
st.subheader("Sections:")

for i, section_title in enumerate(data.keys()):
    with st.expander(section_title.replace("\t", "").upper()):
        section = data[section_title]  
        try:
            suffix = section["suffix"]  
        except:
            suffix = ""
        try:
            additonal_caption = section["additional caption"]
        except:
            additional_caption = ""

        if section["type"] == "dropdown" and isinstance(section["options"], list):
            section_line = st.selectbox("", options = section["options"], key = f"{section_title}-{i}")

            if "Choose further" in section_line:
                subsection = section["further"]
                subsection_suffix = section["further"]["suffix"]
                st.caption(subsection["caption"])

                if subsection["type"] == "multiselect" and isinstance(subsection["options"], list):
                    additional_input = st.multiselect("", options = subsection["options"], key = f"{section_title}-{section_line}-subsection")
                    
                    if len(additional_input) >=2:
                        additional_input = ", ".join(additional_input[:-1]) + ", and " + additional_input[-1] + f" {subsection_suffix}"
                        section_line = section_line.replace(" (Choose further)", "") + f" - {additional_input}"
                    elif len(additional_input) ==1:
                        section_line = section_line.replace(" (Choose further)", "") + f"{additional_input} {subsection_suffix}"
                    else:
                        section_line = section_line.replace(" (Choose further)", "")
                    
            elif "Please specify further - subtype" in section_line:
                additional_input = st.text_input("Please specify the subtype", key = f"{section_title}-{section_line} + text_additional")
                section_line = section_line.replace(" (Please specify further - subtype)", "")
                section_line = section_line + f" - {additional_input}" + " subtype"

            elif "Please specify" in section_line:
                section_line = st.text_input("Please specify", key = f"{section_title}-{section_line}")
                if section_line != "":
                    section_line = section_line + " " + section["suffix"]

            if "Cannot be determined (Explain)" in section_line:
                section_line = st.text_input("Cannot be determined due to:", key = f"{section_title}-{section_line}")
                section_line = "Cannot be determined due to "+ section_line
        
        if section["type"] == "multiselect" and isinstance(section["options"], list):
            section_line = st.multiselect("", options = section["options"], key = f"{section_title}-{i}")
            section_line_with_additional = []
            for j, option in enumerate(section_line):
                if "Please specify" in option:
                    end_index = option.find(" (")
                    option = option[:end_index]
                    additional_input = st.text_input(additonal_caption, key = f"{section}-{j}-{section_line}")
                    section_line_with_additional.append(f"{option} ({additional_input})")
                else:
                    
                    section_line_with_additional.append(option)
            section_line = section_line_with_additional
            if len(section_line) >2: 
                section_line = ", ".join(section_line[:-1]) + ", and " + section_line[-1] + " " + suffix
            elif len(section_line) == 2:
                section_line = " and ".join(section_line) + " " + suffix 
            elif len(section_line) == 1: 
                section_line = section_line[0] 
            else:
                section_line = ""

        if section["type"] == "text":
            section_line = st.text_input("", key = f"{section_title}-{i}") 
            if ", " in section_line:
                section_line = section_line.split(", ")
                section_line = ", ".join(section_line[:-1]) + " and " + section_line[-1] + f" {suffix}"

            elif section_line != "":
                section_line = section_line + " " + suffix
            

        col1, col2 = st.columns([1,3])     
        with col1:
            if st.button("Add to Report", key = f"Add to report: {section_title}-{section_line}"):
                st.session_state.protocol_content_thyroid[section_title] = section_line.upper()
                
        with col2:
            if st.button("Remove from Report", key = f"Remove from report: {section_title}-{section_line}"):
                st.session_state.protocol_content_thyroid[section_title] = ""    

        with st.container():
            st.markdown("**Preview:**")
            st.text(f"{section_title}: {st.session_state.protocol_content_thyroid[section_title]}")

        st.caption(data[section_title]["caption"])

with st.expander("ADDITIONAL FINDINGS"):
    additional_findings = st.text_input("Additional Findings:", key = "additional findings")
    additional_findings = additional_findings.split(", ")
    additional_findings[0] = "\n- " + additional_findings[0]
    additional_findings = "\n- ".join(additional_findings)

    col1, col2 = st.columns([1,3])     
    with col1:
        if st.button("Add to Report", key = "Additional findings - add"):
            st.session_state.protocol_content_thyroid["Additional Findings"] = additional_findings.upper()
                
    with col2:
        if st.button("Remove from Report", key = "Additional findings - remove"):
            st.session_state.protocol_content_thyroid["Additional Findings"] = ""    
    
    with st.container():
        st.markdown("**Preview:**")
        st.text(f"Additional Findings: {st.session_state.protocol_content_thyroid['Additional Findings']}")

    st.caption("Please input all additional findings here, each line to be separated by a comma followed by a single white space (, ).")
    
final_report = "\n".join([f"{k}: {v}." for k, v in st.session_state.protocol_content_thyroid.items() if v !=""])
st.subheader(":page_facing_up: Final Report:")
st.text(final_report)
col1, col2 = st.columns([1, 10])
with col1: 
    st_copy_to_clipboard(final_report)  
with col2:
    st.subheader("Copy to clipboard :clipboard:")

st.info(":warning: Please do not forget to paste your report onto a text file before pressing the \"Clear Report\" button.")

clear_report =  st.button("Clear Report", key = "clear report")
if clear_report:
    del st.session_state.protocol_content_thyroid
    st.rerun()



