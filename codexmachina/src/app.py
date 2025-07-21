import streamlit as st
import os
import sys
import platform

# Add the project root to the path to make imports work
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from codexmachina.src.extraction.pdf_parser import extract_text_from_pdf
from codexmachina.src.extraction.docx_parser import extract_text_from_docx
from codexmachina.src.processing.code_detector import detect_code_blocks
from codexmachina.src.processing.text_cleaner import clean_text

# Handle different magic libraries based on platform
try:
    import magic
    has_magic = True
except ImportError:
    has_magic = False
    st.warning("python-magic library not available. File type detection may be limited.")

st.title("CodexMachina - Extracción de Código")

uploaded_file = st.file_uploader("Carga un archivo PDF o DOCX", type=["pdf", "docx"])

if uploaded_file:
    # Determine file type
    if has_magic:
        file_type = magic.from_buffer(uploaded_file.read(1024), mime=True)
        uploaded_file.seek(0)  # reset file pointer
    else:
        # Fallback to extension-based detection
        file_name = uploaded_file.name.lower()
        if file_name.endswith('.pdf'):
            file_type = "application/pdf"
        elif file_name.endswith('.docx'):
            file_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        else:
            file_type = "unknown"

    raw_text = ""
    if file_type == "application/pdf" or file_name.endswith('.pdf'):
        raw_text = extract_text_from_pdf(uploaded_file)
    elif "wordprocessing" in file_type or file_name.endswith('.docx'):
        raw_text = extract_text_from_docx(uploaded_file)

    if raw_text:
        cleaned_text = clean_text(raw_text)
        code_blocks = detect_code_blocks(cleaned_text)

        if code_blocks:
            st.subheader("Código Extraído:")
            for i, block in enumerate(code_blocks, 1):
                st.code(block, language='python')

            st.download_button("Descargar Código", data="\n\n".join(code_blocks), file_name="extracted_code.py", mime="text/plain")
        else:
            st.info("No se detectaron bloques de código en este documento.")
    else:
        st.error("No se pudo extraer texto del documento. Verifica que el formato sea compatible.")