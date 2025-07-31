import re

def detect_code_blocks(text):
    """
    Detecta bloques de código en el texto utilizando múltiples heurísticas.
    
    Args:
        text (str): El texto limpio del que extraer bloques de código
        
    Returns:
        list: Lista de bloques de código encontrados
    """
    code_blocks = []
    
    # 1. Detectar bloques marcados con triples comillas (formato Markdown)
    markdown_pattern = r'```(?:python)?\s*(.*?)\s*```'
    markdown_blocks = re.findall(markdown_pattern, text, re.DOTALL)
    code_blocks.extend(markdown_blocks)
    
    # 2. Detectar bloques con indentación consistente (4+ espacios)
    lines = text.split('\n')
    current_block = []
    in_code_block = False
    
    for line in lines:
        if line.startswith('    ') and line.strip():  # Línea indentada con contenido
            if not in_code_block:
                in_code_block = True
            current_block.append(line.strip())
        elif in_code_block and not line.strip():  # Línea vacía dentro de un bloque
            current_block.append('')
        elif in_code_block:  # Fin del bloque de código
            if len(current_block) > 2:  # Bloques de al menos 3 líneas
                code_blocks.append('\n'.join(current_block))
            current_block = []
            in_code_block = False
    
    # Añadir el último bloque si existe
    if in_code_block and len(current_block) > 2:
        code_blocks.append('\n'.join(current_block))
    
    # 3. Detectar patrones comunes de código Python
    python_patterns = [
        r'def\s+\w+\s*\(.*?\):\s*\n',  # Definiciones de funciones
        r'class\s+\w+(?:\(.*?\))?:\s*\n',  # Definiciones de clases
        r'import\s+[\w\.]+|from\s+[\w\.]+\s+import',  # Importaciones
        r'if\s+.*?:\s*\n.*?(?:elif|else|$)',  # Estructuras if-elif-else
        r'for\s+.*?\s+in\s+.*?:\s*\n',  # Bucles for
        r'while\s+.*?:\s*\n',  # Bucles while
        r'try:\s*\n.*?except',  # Bloques try-except
    ]
    
    for pattern in python_patterns:
        potential_blocks = re.findall(pattern, text, re.DOTALL)
        for block in potential_blocks:
            # Extraer un contexto más amplio alrededor del patrón
            start_idx = text.find(block)
            if start_idx != -1:
                # Buscar el inicio del bloque (línea anterior vacía o inicio del texto)
                context_start = text.rfind('\n\n', 0, start_idx)
                if context_start == -1:
                    context_start = 0
                else:
                    context_start += 2  # Saltar los dos saltos de línea
                
                # Buscar el final del bloque (línea posterior vacía o fin del texto)
                block_end = start_idx + len(block)
                context_end = text.find('\n\n', block_end)
                if context_end == -1:
                    context_end = len(text)
                
                # Extraer el bloque con contexto
                context_block = text[context_start:context_end].strip()
                if len(context_block.split('\n')) > 1:  # Al menos 2 líneas
                    code_blocks.append(context_block)
    
    # Eliminar duplicados y ordenar por longitud (los bloques más largos primero)
    unique_blocks = list(set(code_blocks))
    unique_blocks.sort(key=len, reverse=True)
    
    return unique_blocks

    