import streamlit as st

st.set_page_config(page_title="Step 1: Enter Details", layout="centered")
st.title("📝 Step 1: Enter Resume Rewrite Details")

with st.form("user_details_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    role_or_jd = st.text_area("Target Job Title or Full JD")
    uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    submitted = st.form_submit_button("Continue to Payment")

    if submitted:
        if name and email and role_or_jd and uploaded_resume:
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.role_or_jd = role_or_jd
            st.session_state.resume_file = uploaded_resume
            st.success("✅ Details saved. Go to 'Step 2: Payment' in the sidebar.")
        else:
            st.error("⚠️ Please fill out all fields and upload your resume.")
