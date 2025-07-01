import re

def clean_text(text):
    #eliminar salto de lineas multiples 
    text = re.sub(r'\n{2,}', '\n\n', text)
    #Eliominar caracteres especiales no imprimibles
    text_text.encode('ascii', 'ignore').decode()
    #Eliminar espacios en blanco adicionales
    text = re.sub(r'\s+', ' ', text).strip()
    return text.strip()