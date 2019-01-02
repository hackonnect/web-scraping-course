import requests
from bs4 import BeautifulSoup

website = requests.get('https://hackonnect.github.io/scrape2')
soup = BeautifulSoup(website.content, 'html.parser')

# Let the students explore the nested data structure using inspect element first

# Quick exercise: assign the div with the class 'parent' to a variable called parent
# Solution:

parent = soup.div

# We can find all the children of this outer div through using .contents

print(parent.contents)

# As you can see, this gives you a list with all the child divs, but none of the grandchild divs.
# Let's save all the parent divs in a parents list.

children = parent.contents

# Let's see the length of this list

print(len(children)) # 9

# But wait, isn't there supposed to only be 4 children?
# Let's look at what children actually contains.

print(children)

# As you can see, line break characters ('\n') are also counted as children of this parent div!
# We need to filter these out.
# Exercise: Try to find a way to filter these out and save the final list in children.

# Solution: A lot. As long as the length of the final length is 4, the student probably did something right.

children = list(filter(lambda x: x != '\n', children))
print(len(children))

# We can actually find the parent of each div.child by using .parent (slightly confusing here).
# Here, we are looping through the list of children and printing out the first class of the parent for each child.
# Remember that when you find the ['class'] of something, you get a list of the classes.

for child in children:
    print(child.parent['class'][0])

# As expected, we get 4 parents. This is because when we loop through each of the 4 children, and their (common) parent's class
# is printed out.

# We can also use .next_sibling and .previous_sibling to navigate between siblings on the same level.

for child in children:
    print(child.next_sibling)

# This is not what we are expecting is it? This is because .next_sibling only works on BeautifulSoup objects.
# Earlier on when we made the children variable, we used parent.contents to give us a list of strings of HTML elements.
# In order to get a generator containing BeautifulSoup objects, we need to use parent.children.

children = parent.children # Remember that we did not filter out any of the empty lines this time.
print(children)
for child in children:
    print(child.next_sibling)

# Now this gives us our intended outcome.
# If we want a generator containing BeautifulSoup objects of the next siblings, we can use .next_siblings
# Note: remember that if you use .children etc. the thing you get is NOT a list. It's a list_iterator / generator that
# should only be used when iterating through them.

for next_sibling in parent.div.next_siblings:
    print('I\'m another sibling!')

# Have a few minutes to experiment with everything we have so far.
# We'll showcasing real life applications of web scraping with a more practical example very soon.
