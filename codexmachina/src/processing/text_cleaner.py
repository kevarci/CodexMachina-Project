import re

def clean_text(text):
    """
    Limpia el texto eliminando caracteres no ASCII y realizando otras operaciones
    de limpieza necesarias.
    
    Args:
        text (str): El texto a limpiar
        
    Returns:
        str: El texto limpio
    """
    # Corregido: text_text → text
    cleaned_text = text.encode('ascii', 'ignore').decode()
    
    # Eliminar espacios en blanco extras
    cleaned_text = ' '.join(cleaned_text.split())
    
    return cleaned_text