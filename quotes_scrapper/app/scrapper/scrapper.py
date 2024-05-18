from app.utils.web_extractor import web_data_extractor

class Scrapper:

    def __init__(self, url:str) -> None:
        self._url = url
    
    def scrape_data(self):
        data = web_data_extractor(self._url)
        return data