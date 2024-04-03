from bs4 import BeautifulSoup, Tag

s = ' <div id="foo">foo <i>foo</i> hi foo hi</div>'

soup = BeautifulSoup(s, "html.parser")

for el in soup.find():
    p = Tag(soup, "p")  # create a P element
    el.replace_with(p)
