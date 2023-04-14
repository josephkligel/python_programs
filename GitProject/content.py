from bs4 import BeautifulSoup
import requests
import lxml
import sys

# Class to scrape data from a provided url and print it in body or paragraphical formats
class Content(BeautifulSoup):
    def __init__(self, url='google.com', headers=None):
        self.response = requests.get(url, headers=headers)
        super().__init__(self.response.text, 'lxml')

    def printBody(self):
        print(self.body.prettify())

    def printParagraphs(self):
        print(self.p.prettify())

