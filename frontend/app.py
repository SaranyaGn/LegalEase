import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests
import streamlit as st
from dotenv import load_dotenv
from document_utils.formatters import format_docx, format_pdf, format_html_preview

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
LOGO_PATH = os.path.join("assets", "logo.png")

st.set_page_config(page_title="LegalEase", layout="centered", page_icon="⚖️")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, use_container_width=True)
    else:
        st.title("⚖️ LegalEase")

st.markdown("<h2 style='text-align: center;'>AI Legal Document Generator</h2>", unsafe_allow_html=True)

if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""
if "show_edit" not in st.session_state:
    st.session_state.show_edit = False

doc_type = st.text_input("Document Type (e.g., Agreement, Contract, NDA)", "Freelance Work Contract")
parties = st.text_area("Parties Involved", "Jane Doe (Service Provider), TechNova Inc. (Client)")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)", "Work must be delivered by May 15, 2025; Payment within 7 days of invoice.")
dates = st.text_input("Effective Date", "April 15, 2025")

if st.button("Generate Document", type="primary"):
    with st.spinner("Generating document with Gemini..."):
        try:
            payload = {
                "document_type": doc_type,
                "parties": parties,
                "terms": terms,
                "dates": dates
            }
            res = requests.post(f"{BACKEND_URL}/generate", json=payload)
            if res.status_code == 200:
                st.session_state.generated_text = res.json().get("document", "")
                st.success("Document Generated Successfully!")
            else:
                st.error(f"Error: {res.text}")
        except Exception as e:
            st.error(f"Connection failed: {e}")

if st.session_state.generated_text:
    st.markdown("### Document Preview")
    html_content = format_html_preview(st.session_state.generated_text)
    st.markdown(
        f"<div style='border: 1px solid #374151; padding: 16px; border-radius: 8px; background-color: #1F2937; max-height: 400px; overflow-y: auto;'>"
        f"{html_content}</div>",
        unsafe_allow_html=True
    )

    if st.button("📝 Click to Edit Document"):
        st.session_state.show_edit = not st.session_state.show_edit

    if st.session_state.show_edit:
        edited_text = st.text_area("Edit Document Below:", value=st.session_state.generated_text, height=300)
        st.session_state.generated_text = edited_text

    st.markdown("### Export Options")
    col_a, col_b, col_c = st.columns(3)
    file_stub = doc_type.replace(" ", "_").lower()

    with col_a:
        st.download_button(
            "📄 Download as .TXT",
            data=st.session_state.generated_text,
            file_name=f"{file_stub}.txt",
            mime="text/plain"
        )

    with col_b:
        docx_data = format_docx(st.session_state.generated_text, doc_type, LOGO_PATH if os.path.exists(LOGO_PATH) else None)
        st.download_button(
            "📝 Download as .DOCX",
            data=docx_data,
            file_name=f"{file_stub}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    with col_c:
        pdf_data = format_pdf(st.session_state.generated_text, doc_type, LOGO_PATH if os.path.exists(LOGO_PATH) else None)
        st.download_button(
            "📕 Download as .PDF",
            data=pdf_data,
            file_name=f"{file_stub}.pdf",
            mime="application/pdf"
        )