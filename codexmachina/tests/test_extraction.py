def test_pdf_extraction():
    text = extract_text_from_pdf("text_doc.pdf")
    assert "import streamlit" in text 
    