import re

def verifica_formato(string):
    # Expressão regular para verificar os formatos
    regex = r'\$((\d{1,3}(,\d{3})*)|(\d+ dollars)|(\d+ USD))(\.\d{1,2})?'

    # Verifica se a string corresponde ao padrão
    if re.match(regex, string):
        return True
    else:
        return False

# Exemplos de strings
strings = ["$11.2", "$111,111.11", "11 dollars", "11 Ud", "111.111.11", "12 USD"]

# Verifica cada string
for s in strings:
    if verifica_formato(s):
        print(f"A string '{s}' possui um dos formatos especificados.")
    else:
        print(f"A string '{s}' não possui um dos formatos especificados.")
