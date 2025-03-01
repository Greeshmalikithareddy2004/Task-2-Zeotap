import requests
from bs4 import BeautifulSoup
import json

CDP_DOCS = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def scrape_docs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    texts = [p.text for p in soup.find_all("p")]
    return " ".join(texts)

def index_docs():
    data = {cdp: scrape_docs(url) for cdp, url in CDP_DOCS.items()}
    with open("data/cdp_docs.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    index_docs()
