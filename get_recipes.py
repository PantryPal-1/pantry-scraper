# Import the required libraries 
import pandas as pd
from bs4 import BeautifulSoup 
import requests
import time 

# Define the url in python 
baseUrl = "https://www.jamieoliver.com"
url = "https://www.jamieoliver.com/recipes/category/course/mains/"

# Fetching html from the website
page = requests.get(url)
# BeautifulSoup enables to find the elements/tags in a webpage 
soup = BeautifulSoup(page.text, "html.parser")



# GET URLS to all recipes available on main HTML Page
links = []
for link in soup.find_all('a'):
	path = link.get('href')
	if path[0:9] == '/recipes/':
		links.append(path)
print(links)
#
# Parse through each link and make sure its a recipe link


#store in CSV data set





