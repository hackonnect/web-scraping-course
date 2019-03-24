# Wikipedia is one of our most used websites. Whether you'd like to admit it or not, we all use Wikipedia to get information.
# Let's say we want to get the standard atomic weight of every single element.
# Using Wikipedia and BeautifulSoup, we can easily retrieve this information. Try to do it on your own before asking for help.
# You might not have enough time to finish it. Have fun!
# Feel free to carry on working on this in your free time. Computer Science can be fun!

# SAMPLE PROGRAM:

import requests, bs4
soup = bs4.BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/List_of_chemical_elements').content, 'html.parser')
table_rows = soup.find('table', 'wikitable').find_all('tr')[3:-1]
atomic_weight = [0] * 118
for index, row in enumerate(table_rows):
    td = row.select_one('td:nth-of-type(7)')
    if td.span:
        while td.span.sup:
            td.span.sup.decompose()
        atomic_weight[index] = td.span.string
    else:
        while td.sup:
            td.sup.decompose()
        atomic_weight[index] = td.string

print(atomic_weight)