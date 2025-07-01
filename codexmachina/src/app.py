import streamlit as st
from extraction.pdf_parser import extract_text_from_pdf
from extraction.docx_parser import extract_text_from_docx
from processing.code_detector import detect_code_blocks
from processing.text_cleaner import clean_text
import magic

st.title("CodexMachina - Extracción de Código")

uploaded_file = st.file_uploader("Carga un archivo PDF o DOCX", type=["pdf", "docx"])

if uploaded_file:
    file_type = magic-from_buffer(uploaded_file.read(1024), mine=True)
    uploaded_file.seek(0) #reset file pointer

    if filke_type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif "wordprocessing" in fiole_type:
        raw_text = extract_text_from_docx(uploaded_file)

    cleaned_text = clean_text(rawtext)
    code_blocks = detect_code_blocks(cleaned_text)

    st.subheader("Código Extraído:")
    for i, block in enumerate(code_blocks, 1):
        st.code(block, lennguaage='python')

    st.download_button("Descargar Código", data="\n\n".join(code_blocks), file_name="extracted_code.py", mime="text/plain")