'''
Name: Thais Alvarenga
Course: NY Times Highlights and Latest News
Description:  Web scrapper that gets the latest and highlited news from the NY Times's Tech section and saves the title and url for the articles into a csv file. 
Date: 10/11/2023
'''


from bs4 import BeautifulSoup
import requests

# url: https://news.ycombinator.com/
# go to https://news.ycombinator.com/robots.txt to know what this website allows you to do

response = requests.get("https://news.ycombinator.com/")
# this will print all of the html
# print(response.text)

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title)

print()

# this is one way to get the anchor tag inside span with class titleline
article_span = soup.find_all(name="span", class_="titleline")

articles = []

for article in article_span:

    articles.append(article.a)

# this a another way to do it
# articles = soup.select("span.titleline a")

articles_titles = []
articles_links = []

for article in articles:

    articles_titles.append(article.getText())
    # get the attribute href
    articles_links.append(article.get("href"))


articles_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

most_votes = max(articles_votes)
# save the index of the maximum amount of votes
index_most_votes = articles_votes.index(most_votes)

print(articles_titles[index_most_votes])
print(articles_links[index_most_votes])
print(articles_votes[index_most_votes])