# Terminal
# python -m pip install beautifulsoup4
# python -m pip show beautifulsoup4
# python -m pip install --upgrade beautifulsoup4
# python -m pip uninstall beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML", "html.parser")
print(soup.prettify())
