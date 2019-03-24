import requests
from bs4 import BeautifulSoup

website = requests.get('https://hackonnect.github.io/scrape3')
soup = BeautifulSoup(website.content, 'html.parser')

# Sometimes, we need to find the third, fourth, seventh or even forty-second element.
# To do this, we need to first know how CSS selectors work with BeautifulSoup.

# The following code does the exact same thing as soup.find_all('p'), except it uses CSS selectors.
# If possible, always use find_all() as it is significantly faster.

print(soup.select('p'))

# Here are a few things about CSS selectors that will come in handy:

# This selects every p that is inside a div

print(soup.select('div p'))

# This selects every p that is directly under a div.

print(soup.select('div > p'))

# Finding everything with a class of example.

print(soup.select('.example'))

# Finding the third paragraph

print(soup.select('p:nth-of-type(3)'))

# You can also only select the first one using select_one().
# Because select gives you a list, you can use select_one() to just get a single one.

print(soup.select_one('p:nth-of-type(3)'))

# Sometimes, different HTML elements will affect our code.
# Look at the last paragraph with a class of 'broken'. 
# This paragraph, is quite literally, broken.
# If you try to extract the text from the paragraph by appending .string, you'll find that it doesn't work.
# We need to remove everything else that is inside the p.
# If you inspect the element, you'll find that there is also a span inside. We should try to remove the span.

soup.select_one('.broken').span.decompose()

# Decomposing the element will remove it. If we want to keep the value in another variable after decomposing.
# We can do the following:

new_variable = soup.select_one('.broken').span.extract()

# The code above will not work now because we've already decomposed it, but if you have not removed it yet,
# extracting is a very useful tool.