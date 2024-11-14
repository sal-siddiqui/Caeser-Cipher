from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://www.scrapethissite.com/pages/forms/"
page = requests.get(url)

parser = BeautifulSoup(markup=page.text, features="html.parser")
content = parser.find_all("th")

if isinstance(content, list):
    prettified_html = "".join(
        [f"<!-- {i} -->\n" + str(tag.prettify()) for i, tag in enumerate(content)]
    )
else:
    prettified_html = content.prettify()

with open("output.html", "w") as writer:
    writer.write(prettified_html)

# print(content.text.strip())
for item in content:
    print(item.text.strip())
