import requests
from bs4 import BeautifulSoup
url = "https://indianexpress.com/"
r = requests.get(url)

soup = BeautifulSoup(r.text,"html.parser")

for heading in soup.find_all("h2"):
    print(heading.text)
