def detect_code_blocks(text):
    #Detectar boques de codigo entre '''
    code_pattern = r'```(.*?)```'
    code_blocks = re.findall(code_pattern, text, re.DOTALL)
    return code_blocks

    