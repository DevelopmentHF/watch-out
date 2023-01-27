import requests, bs4

# Load in telegram bot data
token = '5964357138:AAH5AIqsf5Xyou4Tqyhhe1qTheJae1somy0'
url = f"https://api.telegram.org/bot{token}"

# Load HTML from website
res = requests.get('https://www.brew-watches.com/watches/brew-metric-silver')
res.raise_for_status()

# Import data into BS4 object 
site = bs4.BeautifulSoup(res.text, 'html.parser')

# Selects specific element which says whether or not something is sold out
elems = site.select('.ProductItem-details-excerpt')
isSoldOut = 'Sold out' in elems[0].getText()

# Write specific message based on isSoldOut condition
if isSoldOut:
    message = 'Unfortunately, the Brew Metric Silver watch is still sold out.'
else:
    message = "Quick, the Brew Metric Silver is available!\nGet it here: https://www.brew-watches.com/watches/brew-metric-silver"

# Send message through telegram
params = {"chat_id": "5772138282", "text": message}
r = requests.get(url + "/sendMessage", params=params)
