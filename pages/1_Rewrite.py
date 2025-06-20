import streamlit as st

st.set_page_config(page_title="Resume Rewrite", layout="centered")
st.title("💼 Get Your Resume Rewritten for ₹51")

st.markdown("Improve your resume's ATS score with help from our team.")

st.markdown("### Step 1: Pay ₹51")
st.markdown("<a href='https://buy.stripe.com/test_link' target='_blank'><button style='padding:10px 20px;margin:10px 0;background:#f39c12;color:white;border:none;border-radius:5px;'>Pay ₹51 Now</button></a>", unsafe_allow_html=True)

st.markdown("### Step 2: Submit Your Details")

with st.form("rewrite_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    target_role = st.text_input("Target Job Role")
    notes = st.text_area("Anything specific to include?")
    resume_upload = st.file_uploader("Upload Resume for Rewrite (PDF)", type=["pdf"])
    submitted = st.form_submit_button("Submit My Details")

    if submitted:
        if name and email and resume_upload:
            st.success("✅ Details submitted! Our team will get back to you with an updated resume.")
        else:
            st.error("⚠️ Please fill in all required fields and upload your resume.")
