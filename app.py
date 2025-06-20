import streamlit as st
import pdfplumber
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="ATS Resume Analyzer", layout="centered")
st.title("📄 Free ATS Resume Checker")

st.markdown("""
Upload your resume and job description to check your ATS match score. If you're not happy with the result, you can opt for a ₹51 resume rewriting service.
""")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def clean(text):
    return re.sub(r"[^a-zA-Z0-9 ]", " ", text).lower()

def compute_score(resume, jd):
    vect = CountVectorizer().fit_transform([resume, jd])
    return round(cosine_similarity(vect)[0][1] * 100, 2)

if resume_file and job_description:
    resume_text = clean(extract_text_from_pdf(resume_file))
    jd_text = clean(job_description)
    score = compute_score(resume_text, jd_text)

    st.success(f"✅ ATS Match Score: {score}%")

    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())
    matched = resume_words & jd_words
    missing = jd_words - resume_words

    st.markdown("### ✅ Matched Keywords")
    st.write(", ".join(list(matched)[:50]))

    st.markdown("### ❌ Missing Keywords")
    st.write(", ".join(list(missing)[:20]))

    st.markdown("---")
    st.markdown("### 📈 Want a Better Score?")
    st.info("Pay ₹51 and get a professionally rewritten ATS-optimized resume.")
    st.markdown("""
    <a href="#resume-form" style="text-decoration:none">
        <button style="padding:10px 20px;background:#27ae60;color:white;border:none;border-radius:5px;font-weight:bold;">Get My Resume Fixed for ₹51</button>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<hr><h2 id='resume-form'>💼 Submit Details for Rewrite</h2>", unsafe_allow_html=True)
st.markdown("Please make the ₹51 payment before submitting.")
st.markdown("<a href='https://buy.stripe.com/test_link' target='_blank'><button style='padding:10px 20px;margin:10px 0;background:#f39c12;color:white;border:none;border-radius:5px;'>Pay ₹51 Now</button></a>", unsafe_allow_html=True)

with st.form("rewrite_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    target_role = st.text_input("Target Job Role")
    notes = st.text_area("Anything specific to include?")
    resume_upload = st.file_uploader("Upload Resume for Rewrite (PDF)", type=["pdf"], key="rewrite_resume")
    submitted = st.form_submit_button("Submit My Details")

    if submitted:
        if name and email and resume_upload:
            st.success("✅ Details submitted! Our team will get back to you with an updated resume.")
        else:
            st.error("⚠️ Please fill in all required fields and upload your resume.")
