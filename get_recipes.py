# Import the required libraries 
import pandas as pd
from bs4 import BeautifulSoup 
import requests
import time 

# Define the url in python 
url = "https://www.jamieoliver.com/recipes/category/course/mains/"

# Fetching html from the website
page = requests.get(url)
# BeautifulSoup enables to find the elements/tags in a webpage 
soup = BeautifulSoup(page.text, "html.parser")

print(soup)

# GET URLS to all recipes available on main

#parse each URL, use recipe-scraper library to get ingredients

#store in CSV data set


