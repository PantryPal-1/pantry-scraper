# Web Scraping Recipes from JamieOliver.com and Allrecipes.com

This Python script is designed to scrape recipe data from [JamieOliver.com](https://www.jamieoliver.com) and [All Recipes](https://www.allrecipes.com). 

Each recipe is represented by a row in the CSV file, with columns for the recipe's URL, title, and list of ingredients.

## Libraries Used
- `pandas`: For handling data in a flexible way.
- `BeautifulSoup`: To parse HTML and XML documents and extract information.
- `requests`: To send HTTP requests, in this case to fetch the HTML content of the website.
- `recipe_scrapers`: To conveniently extract recipe details like title and ingredients.
- `csv`: To write the scraped data to a CSV file.

## How to Use
1. Make sure you have installed all the libraries mentioned above. If not, you can install them using pip:
```
pip install pandas beautifulsoup4 requests recipe-scrapers
```
2. Run the script in your Python environment.
3. Once the script finishes running, you should find a `recipes.csv` file in the same directory as your script. This file contains the scraped recipes.

## Important Notes
- The script fetches recipes from the "mains" category of the website. If you wish to fetch recipes from other categories, you can replace the URL in the `url` variable accordingly.
- Make sure to comply with the website's `robots.txt` rules and the website's terms of service when web scraping.
- This script doesn't handle pagination. It only fetches recipes available on the first page of the specified category. You might need to modify the script if you wish to fetch recipes from all pages in the category.
- The script currently checks if the URL path starts with `/recipes/` to identify recipe links. Be aware that this approach might not be fully accurate and may exclude some recipes or include some non-recipe links.
- The script ignores any exceptions during the scraping process and continues to the next recipe. Depending on your needs, you might want to handle these exceptions differently.
