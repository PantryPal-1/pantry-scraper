# Import the required libraries 
import pandas as pd
from bs4 import BeautifulSoup 
import requests
from recipe_scrapers import scrape_me
import csv

# Define the url in python 
baseUrl = "https://www.jamieoliver.com"
url = "https://www.jamieoliver.com/recipes/category/course/mains/"

# Fetching html from the website
page = requests.get(url)
print(page)

# BeautifulSoup enables to find the elements/tags in a webpage 
soup = BeautifulSoup(page.text, "html.parser")

# Open the CSV file in append mode
csvfile = open('recipes.csv', 'a', newline='')
writer = csv.writer(csvfile)

# Write the header
writer.writerow(["Link", "Title", "Ingredients"])

# GET URLS to all recipes available on main HTML Page
links = []
for link in soup.find_all('a'):
    path = link.get('href')
    if path[0:9] == '/recipes/':
        links.append(baseUrl + path) # add all recipe paths within Jamie oliver

# Parse through each link and make sure its a recipe link
for recipeLink in links:
    scraper = scrape_me(recipeLink)
    try:
        scraper.title()
    except Exception as e:
        continue

    try:
        ingredients = scraper.ingredients()
        title = scraper.title()
        print(title)
        print(ingredients)
        # Write the scraped data to the CSV file
        writer.writerow([recipeLink, title, ingredients])
    except Exception as e:
        continue

csvfile.close()




