'''
Name: Thais Alvarenga
Course: NY Times Highlights and Latest News
Description:  Web scrapper that gets the latest and highlited news from the NY Times's Tech section and saves the title and url for the articles into a csv file. 
Date: 10/11/2023
'''

from bs4 import BeautifulSoup
import requests
import csv

# url we are getting the data from
url = "https://www.nytimes.com/section/technology"

# request from url and get text
response = requests.get(url)
nytimes = response.text

# start beautiful soup 
ny_soup = BeautifulSoup(nytimes, "html.parser")
#print(ny_soup)

# get NYTimes' highlighted news 
highlights = ny_soup.select(selector="h3 a")
# get NYTimes' latest news 
latest = ny_soup.select(selector="a.css-8hzhxf")

# create csv file to store article information
csv_file = open("nytimes_tech_news.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "URL", "Type"])

# write highlighted news into file
for news in highlights:
    # get the title and url
    title = news.string
    url = "https://www.nytimes.com" + news.get("href")

    # store title and url in csv file
    csv_writer.writerow([title, url, "highlight"])

# write latest news into file
for news in latest:
    # get the title and url
    title = news.string
    url = "https://www.nytimes.com" + news.get("href")

    # store title and url in csv file
    csv_writer.writerow([title, url, "latest"])

# close file and print confirmation message
csv_file.close()
print("CSV file created successfully.")

# Print information that we got
print()
print("NYTimes latest new in Tech: ")
print()

# print(highlights)
for news in highlights:
    print(news.string)
    print("https://www.nytimes.com" + news.get("href"))
    print()


# print(latest)
for news in latest:
    print(news.string)
    print("https://www.nytimes.com" + news.get("href"))
    print()




    