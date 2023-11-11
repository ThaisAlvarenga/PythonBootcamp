from bs4 import BeautifulSoup

with open('website.html', 'r') as file:
    contents = file.read()

# if html.parser doesn't work, try lxml, another markup language for websites
soup = BeautifulSoup(contents, 'html.parser')

print("This is everything in tag: ", soup.title)
print("This is the tag name: " , soup.title.name)
print("This is the string inside the tag: " , soup.title.string)

print()
# print all the soup (all the html)
print(soup.prettify())

print()

# prints the first html tag it finds
print("Find first a tag: ", soup.a)

# gives us all anchor tags

all_anchor_tags = soup.find_all(name="a")
print("Find all anchor tags <a>: ", all_anchor_tags)

# Find all returs a list of all the tags found, with each tag being an item
print("Print 2nd anchor tag: ", all_anchor_tags[1])

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

print()

# you can also find things with their ID's and class names
heading1 = soup.find(name="h1", id="name")
# with classes you have to write class_ because class is a reserved word
heading3 = soup.find(name="h3", class_="heading")

print("Heading h1 text: ", heading1.getText())
print("Heading h3 class: ", heading3.get("class"))

print()

# we can also get information by using the tags like the css stylesheet
# this code gets the anchor tag inside a paragraph
url = soup.select_one(selector="p a")
print("Url: " , url)
# you can also use ID's like in
name = soup.select_one(selector="#name")
print("Name: ", name)

# to select all elements with those tags do
headings = soup.select(".heading")
print("Headings: ", headings)