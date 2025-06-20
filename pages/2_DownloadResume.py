import streamlit as st
import pdfplumber
import re
from fpdf import FPDF
import tempfile
import uuid

st.set_page_config(page_title="Download Resume", layout="centered")
st.title("📄 Download Your ATS Ready Resume")

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def clean(text):
    return re.sub(r"[^a-zA-Z0-9 ]", " ", text).lower()

def extract_keywords(text):
    return set(clean(text).split())

def build_pdf(content, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content:
        pdf.multi_cell(0, 10, line)
    path = os.path.join(tempfile.gettempdir(), filename)
    pdf.output(path)
    return path

if "resume" in st.session_state and "jobtitle" in st.session_state:
    resume_text = extract_text_from_pdf(st.session_state.resume)
    jd_text = st.session_state.jobtitle
    resume_words = extract_keywords(resume_text)
    jd_words = extract_keywords(jd_text)
    missing = jd_words - resume_words

    final_content = [
        f"{st.session_state.name}",
        f"Email: {st.session_state.email} | Phone: +91-9876543210 | Location: India",
        "",
        "Professional Summary:",
        "Experienced professional with proven expertise. Proficient in " + ", ".join(list(missing)[:6]) + ".",
        "",
        "Skills:",
        ", ".join(sorted(jd_words)),
        "",
        "Experience:",
        "- Created and executed test cases",
        "- Collaborated with development teams",
        "",
        "Education:",
        "B.Tech in Computer Science, XYZ University (2015 - 2019)"
    ]

    pdf_file = build_pdf(final_content, f"ATS_Resume_{uuid.uuid4()}.pdf")
    with open(pdf_file, "rb") as f:
        st.download_button("📥 Download ATS Ready Resume", f, file_name="ATS_Optimized_Resume.pdf", type="primary")
else:
    st.warning("Please complete previous steps to generate resume.")
