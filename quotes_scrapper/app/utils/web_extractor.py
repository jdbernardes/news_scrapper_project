from typing import Dict, List

import requests
from bs4 import BeautifulSoup


def web_data_extractor(url: str) -> List[Dict[str, str]]:
    extracted_data: List[Dict[str, str]] = []

    # Faz a requisição para a página
    response = requests.get(url)
    if response.status_code == 200:
        # Parseia o conteúdo HTML da resposta
        soup = BeautifulSoup(response.content, "html.parser")
        quotes = soup.find_all("div", class_="quote")
        text, author, tags = [],[],[]

        for quote in quotes:
            text.append(quote.find("span", class_="text").text.strip())
            author.append(quote.find("small", class_="author").text.strip())
            tags.append([tag.text.strip() for tag in quote.find("div", class_="tags").find_all("a")])

        for quote, author, tag in zip(text, author, tags):
          extracted_data.append({
              "quote": quote,
              "author": author,
              "tag": tag
          })
    else:
        print(f"Erro ao acessar {url}")

    return extracted_data
