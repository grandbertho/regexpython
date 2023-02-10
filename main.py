import re

fraz = "Michel #Bertho est un bon #programmeur"
pattern = "#\w+"

nfraz= re.sub(pattern, lambda x: f"<a href=''>{x.group()}</a>", fraz)
print(nfraz)