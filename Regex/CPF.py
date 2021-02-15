import re

#First version
def isValidCPFPattern_V1(CPF):
    pattern = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    #r"\d{3}\.\d{3}\.\d{3}-\d{2}"
    return bool(re.search(pattern,CPF))

#Improving above version
def isValidCPFPattern_V2(CPF):
    pattern = r"^(\d{3}.){2}\d{3}-\d{2}$"
    return bool(re.search(pattern,CPF))

doc = "111.111.111-55"
print(isValidCPFPattern_V1(doc))
print(isValidCPFPattern_V2(doc))
