import re

def detect_code_blocks(text):
    """
    Detecta bloques de código en el texto utilizando expresiones regulares.
    
    Args:
        text (str): El texto limpio del que extraer bloques de código
        
    Returns:
        list: Lista de bloques de código encontrados
    """
    # Patrón para detectar bloques de código (puede necesitar ajustes)
    code_pattern = r'```(?:python)?\s*(.*?)\s*```'
    
    # Buscar todos los bloques de código
    code_blocks = re.findall(code_pattern, text, re.DOTALL)
    
    return code_blocks

    