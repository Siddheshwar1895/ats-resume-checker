import streamlit as st

st.set_page_config(page_title="Upgrade Resume", layout="centered")
st.title("🔁 Upgrade Resume")

with st.form("upgrade_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    jobtitle = st.text_input("Job Title or JD")
    resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    submitted = st.form_submit_button("Build ATS Match Resume")

    if submitted:
        if name and email and jobtitle and resume:
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.jobtitle = jobtitle
            st.session_state.resume = resume
            st.success("✅ Resume data received. Proceed to payment.")
        else:
            st.error("⚠️ All fields are required.")

if "resume" in st.session_state:
    st.markdown("---")
    st.markdown("### 💳 Payment Details (₹51)")
    st.markdown("""
    - 💳 Card / Netbanking / UPI accepted  
    - Bill Amount: ₹51  
    - (Simulated for now)
    """)
    st.session_state.paid = True
    st.page_link("pages/2_DownloadResume.py", label="Proceed to Download", icon="📥")
