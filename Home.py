import streamlit as st
import pdfplumber
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title='ATS Checker', layout='centered')
st.title('📄 ATS Resume Checker')

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description or Job Title")
match_clicked = st.button("Match")

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def clean(text):
    return re.sub(r"[^a-zA-Z0-9 ]", " ", text).lower()

def compute_score(resume_text, jd_text):
    documents = [resume_text, jd_text]
    vect = CountVectorizer().fit_transform(documents)
    return round(cosine_similarity(vect)[0][1] * 100, 2)

if match_clicked and resume_file and job_description:
    resume_text = clean(extract_text_from_pdf(resume_file))
    jd_text = clean(job_description)
    score = compute_score(resume_text, jd_text)

    st.markdown(f"""<h2 style='color:green;'>✅ ATS Match Score: <span style='font-size:28px;'>{score}%</span></h2>""", unsafe_allow_html=True)

    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())
    matched = resume_words & jd_words
    missing = jd_words - resume_words

    st.subheader("✅ Matched Keywords")
    st.write(", ".join(list(matched)[:50]))
    st.subheader("❌ Missing Keywords")
    st.write(", ".join(list(missing)[:20]))

    st.markdown("---")
    st.info("Want to improve your ATS score to 100%?")
    st.page_link("pages/1_UpgradeResume.py", label="Upgrade My Resume", icon="🔁")
elif match_clicked:
    st.warning("Please upload a resume and enter a JD or job title.")
