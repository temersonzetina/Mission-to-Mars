
# Import dependencies.

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Enable Flask to create a template and a URL for your site.
from flask import Flask, render_template, redirect, url_for

# Make it possible Flask and Mongo interact with one another.
from flask_pymongo import PyMongo

# We will convert from Jupyter to Python to scrape.
import scraping

# Set up Flask.
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection.
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for the web page.
@app.route("/")

# Define the home page, index.html. This links the visual web app to our code.
def index():
   mars = mongo.db.mars.find_one()
   # Return a HTML template using an index.html file.
   return render_template("index.html", mars=mars)

# Define your scraping route.
@app.route("/scrape")
# Create a function to activate your scraping "button."
def scrape():
    # Assign a variable that points to our MongoDB database.
    mars = mongo.db.mars
    # Create a variable to hold the scraped data.
    mars_data = scraping.scrape_all()
    # To update: (1) Insert an empty JSON object that will be filled
    # (2) Use the data stored in mars_data
    # (3) Create a new document if one doesn't already exist
    mars.update({}, mars_data, upsert=True)
    # Navigate back to the the "/" page to see updated content.
    return redirect('/', code=302)

# Tell Flask to run.
if __name__ == "__main__":
       app.run()

