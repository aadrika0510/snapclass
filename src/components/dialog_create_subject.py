import streamlit as st
from src.database.db import create_subject


@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject")

    # Add unique keys to persist state across reruns
    sub_id = st.text_input("Subject Code", placeholder="CS101", key="dialog_sub_id")
    sub_name = st.text_input(
        "Subject Name",
        placeholder="Introduction to Computer Science",
        key="dialog_sub_name",
    )
    sub_section = st.text_input("Section", placeholder="A", key="dialog_sub_section")

    if st.button("Create Subject Now", type="primary", width="stretch"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject Created Successfully!")

                # Optional: Clear the inputs after success
                st.session_state.dialog_sub_id = ""
                st.session_state.dialog_sub_name = ""
                st.session_state.dialog_sub_section = ""

                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all the fields")
