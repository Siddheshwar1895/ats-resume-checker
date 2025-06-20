import streamlit as st

st.set_page_config(page_title="Step 2: Payment", layout="centered")
st.title("💳 Step 2: Make Payment")

if not all(k in st.session_state for k in ["name", "email", "role_or_jd", "resume_file"]):
    st.warning("⚠️ Please complete Step 1 first.")
else:
    st.write("Click the button below to simulate ₹51 payment (testing mode):")
    if st.button("✅ Simulate ₹51 Payment"):
        st.session_state.payment_done = True
        st.success("💰 Payment recorded (test mode). Proceed to download in Step 3.")
