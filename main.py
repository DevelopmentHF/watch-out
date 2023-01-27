import requests, bs4

# Load HTML from website
res = requests.get('https://www.brew-watches.com/watches/brew-metric-silver')
res.raise_for_status()

# Import data into BS4 object 
site = bs4.BeautifulSoup(res.text, 'html.parser')

# Selects specific element which says whether or not something is sold out
elems = site.select('.ProductItem-details-excerpt')
isSoldOut = 'Sold out' in elems[0].getText()

print(isSoldOut)