import streamlit as st
import os
import sys

# Add the project root to the path to make imports work
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from codexmachina.src.extraction.pdf_parser import extract_text_from_pdf
from codexmachina.src.extraction.docx_parser import extract_text_from_docx
from codexmachina.src.processing.code_detector import detect_code_blocks
from codexmachina.src.processing.text_cleaner import clean_text
import magic

st.title("CodexMachina - Extracción de Código")

uploaded_file = st.file_uploader("Carga un archivo PDF o DOCX", type=["pdf", "docx"])

if uploaded_file:
    file_type = magic.from_buffer(uploaded_file.read(1024), mime=True)
    uploaded_file.seek(0)  # reset file pointer

    raw_text = ""
    if file_type == "application/pdf":
        raw_text = extract_text_from_pdf(uploaded_file)
    elif "wordprocessing" in file_type:
        raw_text = extract_text_from_docx(uploaded_file)

    cleaned_text = clean_text(raw_text)
    code_blocks = detect_code_blocks(cleaned_text)

    st.subheader("Código Extraído:")
    for i, block in enumerate(code_blocks, 1):
        st.code(block, language='python')

    st.download_button("Descargar Código", data="\n\n".join(code_blocks), file_name="extracted_code.py", mime="text/plain")