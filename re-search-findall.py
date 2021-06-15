import re

# import L. Frank Baum's The Wonderful Wizard of Oz
oz_text = open("the_wizard_of_oz_text.txt", encoding="utf-8").read().lower()

# search oz_text for an occurrence of 'wizard' here
found_wizard = re.search(r"wizard", oz_text)
print(found_wizard)

# find all the occurrences of 'lion' in oz_text here
all_lions = re.findall(r"lion", oz_text)
print(all_lions)

# store and print the length of all_lions here
number_lions = len(all_lions)
print(number_lions)
