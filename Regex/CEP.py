import re

def isValidCEPPattern_V1(CEP):
    pattern = r"^\d{5}-\d{3}$"
    #r"\d{3}\.\d{3}\.\d{3}-\d{2}"
    return bool(re.search(pattern,CEP))

cep = "11211-500"
print(isValidCEPPattern_V1(cep))

