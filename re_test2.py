import re

# Expressão regular para verificar o formato
regex = r'\$((\d{1,3}(,\d{3})*)|(\d+ dollars)|(\d+ USD))(\.\d{1,2})?'

# Texto completo da string
texto = "SpaceX inks  deal with US, deepening ties to intelligence, military agencies"

# Verifica se a string corresponde ao padrão
if re.search(regex, texto):
    print("A string corresponde ao padrão especificado.")
else:
    print("A string não corresponde ao padrão especificado.")
