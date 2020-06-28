import webbrowser, sys, bs4, lxml, requests

print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
try:
    linkElems = soup.select('.package-snippet')
except Exception as e:
    print('Error', e)

numOpen = min(5, len(linkElems))
#for i in range(numOpen):
#    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
#    print('Opening', urlToOpen)
#    webbrowser.open(urlToOpen)
for i in range(numOpen):
    url = 'https://pypi.org' + linkElems[i].get('href')
    print(url)
    print(linkElems[i].select_one('.package-snippet__name').getText())
    print(linkElems[i].select_one('.package-snippet__description').getText() + '\n')
