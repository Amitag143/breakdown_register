import streamlit as st
import pandas as pd
from datetime import datetime

# Title and Header
st.title("BI MINING INFRA LIMITED")
st.header("JOB CARD ENTRY")

# Session state initialization
if 'breakdown_data' not in st.session_state:
    st.session_state.breakdown_data = []

# Breakdown entry form
with st.form("breakdownentry_form"):
    # Automatically calculate the next Sl No
    sl_no = len(st.session_state.breakdown_data) + 1
    date = st.date_input("Date", value=datetime.now())
    door_no = st.text_input("Door No")
    section = st.selectbox("Section", ["Dumper_section", "Machine_section"])
    job_card_no = st.text_input("Job Card No")
    breakdown_type = st.selectbox("Breakdown Type", ["Electrical", "Mechanical", "leaf_spring", "engine failure"])
    breakdown_description = st.text_area("Breakdown Description")
    in_time = st.time_input("In Time")
    out_time = st.time_input("Out Time")
    action_taken = st.text_area("Action Taken")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.session_state.submitted = True  # Track that the form was submitted
    st.success("Form submitted successfully.")

    # Add the submitted data to the session state
    new_entry = {
        "Sl No": sl_no,
        "Date": date.strftime("%Y-%m-%d"),
        "Door No": door_no,
        "Section": section,
        "Job Card No": job_card_no,
        "Breakdown Type": breakdown_type,
        "Breakdown Description": breakdown_description,
        "In Time": in_time.strftime("%H:%M:%S"),
        "Out Time": out_time.strftime("%H:%M:%S"),
        "Action Taken": action_taken,
    }
    st.session_state.breakdown_data.append(new_entry)

    # Create a DataFrame with all the data
    df = pd.DataFrame(st.session_state.breakdown_data)

    # Display the DataFrame
    st.subheader("Submitted Data")
    st.dataframe(df)

    # Provide a download link for the DataFrame as a CSV file
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Data as CSV",
        data=csv,
        file_name="breakdown_data.csv",
        mime="text/csv",
    )