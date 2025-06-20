import streamlit as st
import pdfplumber
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="ATS Resume Checker", layout="centered")
st.title("📄 ATS Resume Match Checker")

st.markdown("""Upload your resume and job description to get an ATS match score.""")

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

if st.button("Match"):
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
        st.page_link("pages/1_Rewrite.py", label="Get My Resume Fixed for ₹51", icon="💼")
    else:
        st.warning("Please upload a resume and enter a job description.")
