import streamlit as st
import pickle
from st_copy_to_clipboard import st_copy_to_clipboard

st.header("CAP Synoptic Reporting: Oral Cavity (June 2023)")
st.subheader(":eyeglasses: Instructions:")
st.markdown("""
        1. Input all lines you wish to include into the report and then click the **\"Add to Report\"** button. **If a text input field is required in one of the sections, please press "Enter" first after typing in your entry and before clicking the "Add Report" button. Otherwise, it will not be included into the line.** Any line/section left blank will _**not**_ be seen in the final report. *There's no need to worry about the upper/lower case and indentations - this will be reflected in the final report.* Additional notes for each section are included at the end of each section/expandable window.
        2. If you wish to remove a line, click the **\"Remove from Report\"** button. 
        3. A preview of the line will be updated at each section. The text for the final report which can be seen at the end of the page will be updated as you go add/remove each line.
        4. The final report will be previewed at the end of all sections. Click the checkbox :clipboard: at the bottom of the page to copy the entire report to your clipboard, and paste it to your chosen text platform. **_Reminder: this app does not save any of your written reports._** So once you've finished with a report, do not forget to copy it and paste it onto a text file somewhere else.
        5. If you want to start over with a new outline, click the **\"Clear Report\"** button.
        6. For **other tissue/organ involvement** - to enumerate individual specimens e.g. \"Fibrocollagenous tissues in the specimens labeled __\", please choose the option \"Specify individually\" and input the each specimen accordingly.
        7. For **regional lymph node status - to enumerate individual lymph node specimens e.g. \" positive for tumor: - x out of y lymph node(s) in the specimen labeled 'external lymph nodes' \", please choose the option \"Specify individually\" and input each specimen accordingly.
            """)

with open("data/oral_jun2023.pkl", 'rb') as fp:
    data = pickle.load(fp)

if "protocol_content_oral" not in st.session_state:
    st.session_state.protocol_content_oral = {k:v for k, v in zip(data.keys(), [""] * len(data))}
    st.session_state.protocol_content_oral["Additional Findings"] = "" 

if "ln_counter_positive_oral" not in st.session_state:
    st.session_state.ln_counter_positive_oral = 0

if "ln_counter_negative_oral" not in st.session_state:
    st.session_state.ln_counter_negative_oral = 0

if "organ_pos_counter_oral" not in st.session_state:
    st.session_state.organ_pos_counter_oral = 0

if "organ_neg_counter_oral" not in st.session_state:
    st.session_state.organ_neg_counter_oral = 0

st.divider()
st.subheader("Sections:")

for i, section_title in enumerate(data.keys()):
    with st.expander(section_title.replace("\t", "").upper()):
        section = data[section_title]  
        try:
            caption = section["caption"]
        except:
            caption = ""
        try:
            suffix = section["suffix"]  
        except:
            suffix = ""
        try:
            additonal_caption = section["additional caption"]
        except:
            additional_caption = ""
        
        try:
            further_options = section["further"]
        except:
            further_options = []
        
        if section["type"] == "blank":
            section_line = " "

        if section["type"] == "dropdown-count":
            section_line = st.selectbox("", options = section["options"], key = f"{section_title}-{i}")
            
            if section_line == "Exact number":
                number_ln = st.text_input("Please specify exact number of lymph node(s)", key =  f"{section_title}-{i}-exact")
                section_line = f"{number_ln} {suffix}"+ "."

            elif section_line == "At least":
                number_ln = st.text_input("At least __ number of lymph node(s)", key =  f"{section_title}-{i}-atleast")
                section_line = f"At least {number_ln} {suffix}" + "."

            elif "Please specify" in section_line:
                section_line = st.text_input("Please specify", key = f"{section_title}-{section_line}")
                if section_line != "":
                    section_line = section_line + " " + section["suffix"] + "."

            elif "Cannot be determined (Explain)" in section_line:
                section_line = st.text_input("Cannot be determined due to:", key = f"{section_title}-{section_line}")
                section_line = "Cannot be determined due to "+ section_line+ "."

        if section["type"] == "dropdown-size":
            section_line = st.selectbox("", options = section["options"], key = f"{section_title}-{i}")

            if section_line == "Specify exact size": 
                size_ln = st.text_input(f"{suffix}", key =  f"{section_title}-{i}-exact")
                section_line = f"{size_ln} {suffix}" + "."
            
            elif section_line == "At least":
                size_ln = st.text_input("Please specify size", key =  f"{section_title}-{i}-at least")
                section_line = f"At least {size_ln} {suffix}" + "."

            elif section_line == "Less than":
                size_ln = st.text_input("Please specify size", key =  f"{section_title}-{i}-at least")
                section_line = f"Less than {size_ln} {suffix}" + "."
        
            elif section_line == "Greater than":
                size_ln = st.text_input("Please specify size", key =  f"{section_title}-{i}-greater than")
                section_line = f"Greater than {size_ln} {suffix}" + "."
            
            elif "Please specify" in section_line:
                section_line = st.text_input("Please specify", key = f"{section_title}-{section_line}")
                if section_line != "":
                    section_line = section_line + " " + suffix + "."

            elif "Cannot be determined (Explain)" in section_line:
                section_line = st.text_input("Cannot be determined due to:", key = f"{section_title}-{section_line}")
                section_line = "Cannot be determined due to " + section_line + "."
        
        if section["type"] == "dropdown-distance" and isinstance(section["options"], list):
            
            section_line = st.selectbox("", options = section["options"], key = f"{section_title}-{i}")

            if "Specify exact" in section_line:
                distance = st.text_input(f"Specify exact distance in {suffix}", key = f"{section_title}-{section_line}-exact distance")

                section_line = f"{distance} " + suffix + "."
            
            elif section_line == "Greater than":
                distance = st.text_input("Specify distance greater than __ in millimeters (mm)", key = f"{section_title}-{section_line}-greater than distance")
                section_line = f"Greater than {distance} " + suffix + "."
            
            elif section_line == "At least":
                distance = st.text_input("Specify distance at least __ in millimeters (mm)", key = f"{section_title}-{section_line}-at least distance")
                section_line = f"At least {distance} " + suffix + "."
            
            elif section_line == "Less than":
                distance = st.text_input("Specify distance less than __ in millimeters (mm)", key = f"{section_title}-{section_line}-less than distance")
                section_line = f"Less than {distance} " + suffix + "."
            
            elif "Please specify" in section_line:
                section_line = st.text_input("Please specify", key = f"{section_title}-{section_line}")
                if section_line != "":
                    section_line = section_line + " " + suffix + "."

            elif "Cannot be determined (Explain)" in section_line:
                section_line = st.text_input("Cannot be determined due to:", key = f"{section_title}-{section_line}")
                section_line = "Cannot be determined due to " + section_line + "."

        if section["type"] == "dropdown-depth" and isinstance(section["options"], list):
            section_line = st.selectbox("", options = section["options"], key = f"{section_title}-{i}")

            if section_line == "Specify exact depth":
                distance = st.text_input(f"Specify exact depth in {suffix}", key = f"{section_title}-{section_line}-exact depth")

                section_line = f"{distance} " + suffix + "."
            
            elif section_line == "At least":
                distance = st.text_input("Specify distance at least __ in millimeters (mm)", key = f"{section_title}-{section_line}-at least depth")
                section_line = f"At least {distance} " + suffix + "."

            elif "Please specify" in section_line:
                section_line = st.text_input("Please specify", key = f"{section_title}-{section_line}-specify-exact-depth")
                if section_line != "":
                    section_line = section_line + " " + suffix + "."

            elif "Cannot be determined (Explain)" in section_line:
                section_line = st.text_input("Cannot be determined due to:", key = f"{section_title}-{section_line}-depth")
                section_line = "Cannot be determined due to " + section_line + "."

        if section["type"] == "dropdown" and isinstance(section["options"], list):
            section_line = st.selectbox("", options = section["options"], key = f"{section_title}-{i}")

            # TODO: Add multiselect - Please specify
            if "Choose further" in section_line:
                subsection = section["further"]
                subsection_suffix = section["further"]["suffix"]
                st.caption(subsection["caption"])

                if subsection["type"] == "multiselect" and isinstance(subsection["options"], list):
                    additional_input = st.multiselect("", options = subsection["options"], key = f"{section_title}-{section_line}-subsection")
                    
                    if len(additional_input) >=2:
                        additional_input = ", ".join(additional_input[:-1]) + ", and " + additional_input[-1] + f" {subsection_suffix}"
                        section_line = section_line.replace(" (Choose further)", "") + f" - {additional_input}" + "."
                    elif len(additional_input) ==1:
                        section_line = section_line.replace(" (Choose further)", "") + f"{additional_input} {subsection_suffix}" + "."
                    else:
                        section_line = section_line.replace(" (Choose further)", "") + "."
                    
            elif "Please specify further - subtype" in section_line:
                additional_input = st.text_input("Please specify the subtype", key = f"{section_title}-{section_line} + text_additional")
                section_line = section_line.replace(" (Please specify further - subtype)", "")
                section_line = section_line + f" - {additional_input}" + " subtype" + "."
            
            elif "Please specify site" in section_line or "Please specify site(s)" in section_line:
                additional_input = st.text_input("Please specify the site if applicable, otherwise, may leave blank", key = f"{section_title}-{section_line} + text_additional - site")
                end_index = section_line.find(" (Please specify")
                section_line = section_line[:end_index]

                if additional_input != "":
                    section_line = section_line + f" ({additional_input})" + "."
                else:
                    section_line = section_line + "" + "."
            
            elif "Please specify location" in section_line:
                additional_input = st.text_input("Please specify the site if applicable, otherwise, may leave blank", key = f"{section_title}-{section_line} + text_additional location")
                end_index = section_line.find(" (Please specify")

                section_line = section_line[:end_index]

                if additional_input != "":
                    section_line = section_line + f" ({additional_input})" + "."
                else:
                    section_line = section_line + ""+ "."

            elif "Please specify" in section_line:
                section_line = st.text_input("Please specify", key = f"{section_title}-{section_line}")
                section_line = section_line.split(", ")

                if len(section_line) ==2:
                    section_line = section_line[0] + " and " + section_line[1] + "."
                elif len(section_line) >2:
                    section_line = section_line[0] + ", " + ", ".join(section_line[1:-1]) + " and " + section_line[-1] + "."
                elif len(section_line) == 1:
                    if section["suffix"] != "":
                        section_line = section_line[0] + " " + section["suffix"] + "."
                    else:
                        section_line = section_line[0] + "."
                elif section_line != "":
                    section_line = f"{section_line} " + section["suffix"] + "."
            
            elif "adjacent structure(s) or organ(s) (Specify individually)" in section_line:
                section_line = ""
                additional_input = st.text_input("Input individual organ(s)/structures(s) involved by direct extension separated by a comma and a single white space (\", \")", key = f"{section}-{section_line}-additional")
                additional_input = additional_input.split(", ")

                if len(additional_input) >= 2:
                    section_line = "Directly involves the " + ", ".join(additional_input[:-1]) + f" and {additional_input[-1]}."
                elif (len) == 1:
                    section_line = "Directly involves the " + additional_input[0] + "."
                else:
                    section_line = "Directly invades adjacent structure(s) or organ(s)."

            elif "lymph node(s) (Specify individually)" in section_line:
                end_index = section_line.find(" (")
                section_line = section_line[:end_index]
                st.subheader("Positive Lymph Nodes")
                lines_ln_pos = st.slider("Number of specimens with at least one (1) positive lymph node", 0, 25,1, key = f"{section_title}-{section_line} slider positive")
                st.session_state.ln_counter_positive_oral = lines_ln_pos
                
                if lines_ln_pos >0:
                    section_line = section_line + "\n\tPositive for tumor:"
                st.caption("Input 1) number of positive lymph nodes; 2) total number of lymph nodes in the specimen; and 3) specimen label.")

                for i in range(1, st.session_state.ln_counter_positive_oral+1):
                    st.markdown(f"**Positive for tumor, specimen no. {i}**")
                    col1_pos, col2_pos = st.columns(2)

                    with col1_pos:
                        num_pos_ln = st.text_input("No. of (+) lymph nodes",  key = f"{section_title}-{section_line}+{i} total positive lymph nodes")
                        num_total_ln = st.text_input("Total no. of lymph nodes", key = f"{section_title}-{section_line}+{i} total lymph nodes (but pos)")
                    with col2_pos:
                        extent_pos_ln = st.selectbox("Extent", options = ["Macrometastases", "Micrometastases", "Isolated tumor cells", "Leave blank"], key = f"{section_title}-{section_line}+{i} extent positive lymph nodes")
                        spec_label_pos = st.text_input(f"Specimen label #{i}\n\n", key = f"{section_title}-{section_line}+{i} specimen label - positive")

                    if num_pos_ln == num_total_ln:
                        additional_input = f"all {num_total_ln} lymph node(s)" + " in the specimen labeled " + f"\"{spec_label_pos}\""
                    else:
                        additional_input = f"{num_pos_ln} out of {num_total_ln} lymph node(s)" + " in the specimen labeled " + f"\"{spec_label_pos}\"" 

                    if extent_pos_ln != "Leave blank":
                        additional_input = additional_input + f" ({extent_pos_ln})"

                    section_line = section_line + "\n\t- " + additional_input + "."

                    st.divider()

                st.subheader("Negative Lymph Nodes")
                lines_ln_neg = st.slider("Number of specimens with at least one (1) negative lymph node", 0, 25, 1, key = f"{section_title}-{section_line} slider negative")
                st.session_state.ln_counter_negative_oral = lines_ln_neg
                if lines_ln_neg > 0:
                    section_line = section_line + "\n\tNegative for tumor:"

                for j in range(1, st.session_state.ln_counter_negative_oral+1):
                    st.markdown(f"**Negative for tumor, specimen no. {j}**")
                    col1_neg, col2_neg = st.columns(2)

                    with col1_neg:
                        num_neg_ln = st.text_input("Total No. of lymph nodes",  key = f"{section_title}-{section_line}+{j} total lymph nodes (but neg)")
                    
                    with col2_neg:
                        spec_label_neg = st.text_input(f"Specimen label no. {j}", key = f"{section_title}-{section_line}+{i} specimen label - negative")

                    if num_neg_ln == "1" or num_neg_ln == "one (1)" or num_neg_ln == "one":
                        additional_input = "1 lymph node(s) in the specimen labeled " + f"\"{spec_label_neg}\""
                    else:
                        additional_input = "All " + num_neg_ln + " lymph node(s) in the specimen labeled " + f"\"{spec_label_neg}\""
                    
                    section_line = section_line + "\n\t- " + additional_input + "."

                    st.divider()

            elif "negative for tumor cells (Specify individually)" in section_line or "lymph nodes negative for tumor (Specify individually)" in section_line:
                lines_ln_neg = st.slider("Number of specimens with at least one (1) negative lymph node", 0, 25, 1, key = f"{section_title}-{section_line} slider negative")
                
                end_index = section_line.find(" (")
                section_line = section_line[:end_index]

                st.session_state.ln_counter_negative_oral = lines_ln_neg
                if lines_ln_neg > 0:
                    section_line = section_line + "\n\tNegative for tumor:"

                for j in range(1, st.session_state.ln_counter_negative_oral+1):
                    st.markdown(f"**Negative for tumor, specimen no. {j}**")
                    col1_neg, col2_neg = st.columns(2)

                    with col1_neg:
                        num_neg_ln = st.text_input("Total No. of lymph nodes",  key = f"{section_title}-{section_line}+{j} total lymph nodes (but neg)")
                    
                    with col2_neg:
                        spec_label_neg = st.text_input(f"Specimen label #{j}", key = f"{section_title}-{section_line}+{i} specimen label - negative")

                    if num_neg_ln == "1" or num_neg_ln == "one (1)" or num_neg_ln == "one":
                        additional_input = "1 lymph node(s) in the specimen labeled " + f"\"{spec_label_neg}\""
                    else:
                        additional_input = "All " + num_neg_ln + " lymph node(s) in the specimen labeled " + f"\"{spec_label_neg}\"" 
                    
                    section_line = section_line + "\n\t- " + additional_input + "."

                    st.divider()

            elif "Please specify components" in section_line:
                additional_input = st.text_input("Please specify each component separated by a comma and a single white space e.g. (, )", key = f"{section_title}-{section_line}")
                end_index = section_line.find(" (")
                section_line = section_line[:end_index]
                section_line = section_line + f" - {additional_input}."

            elif "Specify percentage" in section_line:
                section_line = st.text_input("Specify exact percentage (%)", key = f"{section_title}-{section_line}-specify-percentage")
                section_line = section_line + f" {suffix}." 

            elif "Specify extent" in section_line:
                additional_input = st.text_input("Specify extent", key =f"{section_title}-{section_line}")
                end_index = section_line.find(" (")
                section_line = section_line[:end_index]
                section_line = section_line + " to the " + additional_input + "."

            elif "Cannot be determined (Explain)" in section_line:
                section_line = st.text_input("Cannot be determined due to:", key = f"{section_title}-{section_line}")
                section_line = "Cannot be determined due to "+ section_line + "."
            
            elif "Specify type of therapy" in section_line:
                end_index = section_line.find(" (")
                section_line = section_line[:end_index]
                additional_input = st.text_input("Specify type of therapy performed", key = f"{section_title}-{section_line}-type_of_ther")
                section_line = section_line + f": {additional_input}."

            elif "Specify number" in section_line:
                section_line = st.text_input("Specify number", key = f"{section_title}-{section_line}-specify_number")
                section_line = section_line + f" {suffix}."
                
            else:
                section_line = section_line + "."
        
        if section["type"] == "multiselect" and isinstance(section["options"], list):

            section_line = st.multiselect("", options = section["options"], key = f"{section_title}-{i}")
            
            if "Specify individually" in section_line:
                section_line = ""
                st.subheader("Other organs/tissues positive for tumor")
                organ_pos_num = st.slider("Specify number of other tissues/organs submitted in the specimen", 0, 25, 1, key = f"{section_title}-{section_line} other organs positive")
                st.session_state.organ_pos_counter_oral = organ_pos_num

                if organ_pos_num >0:
                    section_line = section_line + "\n\tPositive for tumor:"
            
                for k in range(1, st.session_state.organ_pos_counter_oral+1):
                    st.markdown(f"**Positive for tumor, specimen no {k}**")
                    col1_org, col2_org = st.columns(2)

                    with col1_org:
                        spec_pos_descriptor = st.text_input("Descriptor (e.g. fibrocollagenous tissue/fibroadipose tissue)", key = f"{section_title}-{section_line}  {k} descriptor positive")
                    
                    with col2_org:
                        spec_pos_organ_label = st.text_input(f"Specimen label no. {k}", key = f"{section_title}-{section_line} {k} label positive")
                    
                    if spec_pos_descriptor != "":
                        section_line = section_line + f"\n\t- {spec_pos_descriptor}" + " in the specimen labeled " + f"\"{spec_pos_organ_label}\""
                    else:
                        section_line = section_line + f"\n\t- Specimen labelled " + f"\"{spec_pos_organ_label}\"" + "."

                    st.divider()

                st.subheader("Other organs/tissues negative for tumor")
                organ_neg_num = st.slider("Specify number of other tissues/organs submitted in the specimen", 0, 25, 1, key = f"{section_title}-{section_line} other organs negative")
                st.session_state.organ_neg_counter_oral = organ_neg_num

                if organ_neg_num >0:
                    section_line = section_line + "\n\tNegative for tumor:"

                for l in range(1, st.session_state.organ_neg_counter_oral+1):
                    st.markdown(f"**Negative for tumor, specimen no {l}**")
                    col1_org, col2_org = st.columns(2)

                    with col1_org:
                        spec_neg_descriptor = st.text_input("Descriptor (e.g. fibrocollagenous tissue/fibroadipose tissue)", key = f"{section_title}-{section_line}  {l} descriptor negative")
                    
                    with col2_org:
                        spec_neg_organ_label = st.text_input(f"specimen label no. {l}", key = f"{section_title}-{section_line} {l} label negative")
                    
                    if spec_neg_descriptor != "":
                        section_line = section_line + f"\n\t- {spec_neg_descriptor}" + " in the specimen labeled " + f"\"{spec_neg_organ_label}\"" + "."
                    else:
                        section_line = section_line + f"\n\t- Specimen labelled " + f"\"{spec_neg_organ_label}\"" + "."
                    st.divider()

            else:
                section_line_with_additional = []

                for j, option in enumerate(section_line):
                    if "Please specify" in option:
                        additional_input = st.text_input(additonal_caption, key = f"{section}-{j}-{option}")
                        section_line_with_additional.append(f"{additional_input}")                         

                    elif "Specify laterality" in option:
                        end_index = option.find(" (")
                        option = option[:end_index]
                        additional_input = st.multiselect("Specify Laterality", options = further_options, key = f"{section}-{j}-{option}")
                        section_line_with_additional.append(f"{option} ({additional_input})")

                    elif "Specify extent" in option:
                        end_index = option.find(" (")
                        option = option[:end_index]
                        additional_input = st.text_input("Specify extent: Unifocal - 1 focal area of carcinoma at the margin, <4 mm; \nMultifocal - 2 or more foci of carcinoma at the margin; \nExtensive - carcinoma present at the margin over a broad front (>5 mm)", key =f"{section_title}-{j}-Extent-{section_line}")
                        section_line_with_additional.append(f"{option} ({additional_input})")

                    elif "Please specify margin and extent" in option: # this is for other margins involved
                        end_index = option.find(" (")
                        option = option[:end_index]
                        option = st.text_input(f"{additional_caption}", key =f"{section_title}-{j}-OtherMargin-{section_line}")
                        additional_input = st.text_input("Specify extent: Unifocal - 1 focal area of carcinoma at the margin, <4 mm; \nMultifocal - 2 or more foci of carcinoma at the margin; \nExtensive - carcinoma present at the margin over a broad front (>5 mm)", key =f"{section_title}-{j}-Extent-{section_line}")
                        section_line_with_additional.append(f"{option} ({additional_input})")

                    else:
                        section_line_with_additional.append(option)

                section_line = section_line_with_additional
                if len(section_line) >2: 
                    section_line = ", ".join(section_line[:-1]) + ", and " + section_line[-1] + suffix + "."
                elif len(section_line) == 2:
                    section_line = " and ".join(section_line) + suffix  + "."
                elif len(section_line) == 1: 
                    section_line = section_line[0]  + "."
                else:
                    section_line = ""
            
        if section["type"] == "text":
            section_line = st.text_input("", key = f"{section_title}-{i}") 
            if ", " in section_line:
                section_line = section_line.split(", ")
                section_line = ", ".join(section_line[:-1]) + " and " + section_line[-1] + f" {suffix}" + "."

            elif section_line != "":
                section_line = section_line + " " + suffix + "."

        if section["type"] == "list":
            section_line = st.text_input(f"{caption}", key = {section_title})
            section_line = section_line.split(", ")
            
            if len(section_line) == 1:
                section_line = section_line[0] + f" {suffix}."
            elif len(section_line) == 2:
                section_line = section_line[0] + " and " + section_line[1] + f"{suffix}."
            elif len(section_line) >2:
                section_line = ", ".join(section_line[:-1]) + " and " + section_line[-1] + f"{suffix}."
            


        col1, col2 = st.columns([1,3])     
        with col1:
            if st.button("Add to Report", key = f"Add to report: {section_title}-{section_line}"):
                st.session_state.protocol_content_oral[section_title] = section_line.upper()
                
        with col2:
            if st.button("Remove from Report", key = f"Remove from report: {section_title}-{section_line}"):
                st.session_state.protocol_content_oral[section_title] = ""    

        with st.container():
            st.markdown("**Preview:**")
            st.text(f"{section_title}: {st.session_state.protocol_content_oral[section_title]}")

        st.caption(data[section_title]["caption"])

with st.expander("ADDITIONAL FINDINGS"):
    additional_findings = st.text_input("Additional Findings:", key = "additional findings")
    additional_findings = additional_findings.split(", ")
    additional_findings[0] = "\n- " + additional_findings[0]
    additional_findings = "\n- ".join(additional_findings) + "."

    col1, col2 = st.columns([1,3])     
    with col1:
        if st.button("Add to Report", key = "Additional findings - add"):
            st.session_state.protocol_content_oral["Additional Findings"] = additional_findings.upper()
                
    with col2:
        if st.button("Remove from Report", key = "Additional findings - remove"):
            st.session_state.protocol_content_oral["Additional Findings"] = ""    
    
    with st.container():
        st.markdown("**Preview:**")
        st.text(f"Additional Findings: {st.session_state.protocol_content_oral['Additional Findings']}")

    st.caption("Please input all additional findings here, each line to be separated by a comma followed by a single white space (, ).")
    
final_report = "\n".join([f"{k}: {v}" for k, v in st.session_state.protocol_content_oral.items() if v !=""])
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
    del st.session_state.protocol_content_oral
    st.rerun()