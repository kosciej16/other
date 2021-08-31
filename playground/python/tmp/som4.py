from requests_html import HTMLSession
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.15.2 Chrome/83.0.4103.122 Safari/537.36"
}

session = HTMLSession()

# res = requests.get("https://www.csie.ntu.edu.tw/members/teacher.php?mclass1=110", headers=headers)
r = session.get("https://www.csie.ntu.edu.tw/members/teacher.php?mclass1=110", headers=headers)
r.html.render()
__import__("pdb").set_trace()
print(r.html)
# links = r.html.links
# for l in links:
#     print(l)
# if "@" in l:
#     print(l)

# print(content)
# content = res.content
# with open("tmp", "r+") as f:
#     content = f.read()
# with open("tmp", "w+") as f:
#     f.write(str(content))
# html = etree.HTML(content)

# email = html.xpath("//a/text()")
# print(email)
# for e in email:
#     print(e)
# e
# print(etree.tostring(e))
# break
