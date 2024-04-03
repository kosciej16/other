import re
import regex

r = r"(?b)(North\ West)"
s = "South west South West North West"
# m = re.search(r, s)
# print(m)
x = regex.findall(
    r"(?b)(North\ West){i<=0,s<=2,d<=1}", "North west North West South West South West", regex.V1
)
print(x)
