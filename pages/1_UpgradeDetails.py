import streamlit as st

st.set_page_config(page_title="Upgrade Details", layout="centered")
st.title("🔁 Step 1: Resume Upgrade Details")

with st.form("details_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    jobtitle = st.text_input("Target Job Title or JD")
    resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    submitted = st.form_submit_button("Proceed to Payment")

    if submitted:
        if name and email and jobtitle and resume:
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.jobtitle = jobtitle
            st.session_state.resume = resume
            st.success("✅ Details saved. Now proceed to payment.")
        else:
            st.error("⚠️ Please complete all fields.")

st.markdown("---")
if "name" in st.session_state:
    st.markdown("### 💳 Pay ₹51 to continue")
    st.markdown("<a href='#'><button style='padding:10px 20px;background:#f39c12;color:white;border:none;border-radius:5px;'>Simulated ₹51 Payment</button></a>", unsafe_allow_html=True)
    st.session_state.paid = True
    st.page_link("pages/2_DownloadPDF.py", label="➡️ Continue to Download", icon="📄")
