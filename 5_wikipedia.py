# Wikipedia is one of our most used websites. Whether you'd like to admit it or not, we all use Wikipedia to get information.
# Let's say we want to get the standard atomic weight of every single element.
# Using Wikipedia and BeautifulSoup, we can easily retrieve this information. Try to do it on your own before asking for help.
# You might not have enough time to finish it. Have fun!
# Feel free to carry on working on this in your free time. Computer Science can be fun!

# SAMPLE PROGRAM:

import requests, bs4
soup = bs4.BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/List_of_chemical_elements').content, 'html.parser')
table = soup.find('table', 'wikitable')
atomic_weight = [0] * 118
for i in range(118):
    atomic_weight[i] = table.tbody.select_one('tr:nth-of-type(' + str(i + 3) + ')').select_one('td:nth-of-type(7)').span.string
