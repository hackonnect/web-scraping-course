# In order to request the HTML file of a webpage, we need to use the reqeusts library
import requests

website = requests.get('https://hackonnect.github.io/scrape1')

print(website) # <Response [200]>
print(website.status_code) # 200
print(website.content) # Long string containing HTML

# Import BeautifulSoup first in order to use it
# MAKE SURE BS4 IS INSTALLED
from bs4 import BeautifulSoup

# Now, we can run the file through BeautifulSoup to give us a nested data structure
# The arguments tells BeautifulSoup that this is a HTML document and that a HTML parser should be used
soup = BeautifulSoup(website.content, 'html.parser')

print(soup) # Long string containing HTML

# Calling prettify() on your BeautifulSoup object prints a readable/formatted version of the HTML
print(soup.prettify()) # Long string containing pretty HTML

# We can find each element in our soup by referencing them by their HTML element name
# This gives you their HTML code

print(soup.title) # <title>Practice Web Scraping with Python</title>

# To get the element name, simply add .name at the end

print(soup.title.name) # title

# To get its content, add .string at the end

print(soup.title.string) # Practice Web Scraping with Python

# When you do this, however, you can only get the first HTML element with that name.
# Try it with the different paragraphs on the screen.

print(soup.p) # <p>p</p>

# To get every p, we need to use .find_all(), this gives us a list of HTML elements
# Note the quotation marks outside p when you do this.

print(soup.find_all('p')) # List of paragraphs

# You can get the attributes for different HTML elements. Let's try it on the different paragraphs

paragraphs = soup.find_all('p')

# Let's see the class of the second paragraph (remember that python is 0 indexed)

print(paragraphs[1]['class']) # ['important red']

# Nice! This gives us what we want. Because BeautifulSoup gives us the attribute values in a list,
# we can add [0] to the end of that chain in order to get what we need.

print(paragraphs[1]['class'][0]) # important

# What if an element has multiple values for a single attribute like the red and important paragraph

print(paragraphs[2]['class']) # ['important', 'red']

# To get every single attribute of an element, we can use attrs

print(paragraphs[3].attrs) # {'class': 'important', 'id': 'unique'}

# In order to find a paragraph by its id, you can use .find(id=''). This gives you the first element with this id.
# You can also use .find_all(id='') in order to find all the elements with a particular attribute.

print(soup.find(id='unique')) # <p class="important" id="unique">unique and important</p>
print(soup.find_all(id='unique')[0]) # <p class="important" id="unique">unique and important</p>

# Usually, you want to use find for finding things with specific ids since ids in HTML is almost always unique.
# For everything else, .find_all() is a lot more suitable as you can find every desired element.

# We can find all the divs with a particular class:

print(soup.find_all('div', 'sibling')) # Find all divs with a class of sibling

# Remember how we found specific ids? We can do the same for elements with custom attributes:

print(soup.find_all(name='h1')) # [<h1>h1</h1>]

# You can also pass multiple attributes at once.

print(soup.find_all(name='h1', id='h1')) # [<h1>h1</h1>]

# Another way of writing this:

print(soup.find_all(attrs={'name': 'h1', 'id': 'h1'})) # [<h1>h1</h1>]

# Now try this yourselves: What is the class of the last paragraph of this page!
# Reminder: you can easily get the last item of a python list by using [-1]

# Note: If the students do this the wrong way, they will get a class of you_made_a_mistake.
# Remind them that you can get the lsat item of a python list by using [-1]

# Solution: print(paragraphs[-1]['class'][0])
# Answer: upper
# I hope that everyone got the pun

# There's actually a hidden paragraph that you cannot see on the webpage!
# If you messed up the previous exercise, you might have gotten hidden as a class.
# Try to find out what this paragraph (with an id of 'hidden') says!

# Solution: print(soup.find(id='hidden').string)
# Answer: # Hidden from your sight
