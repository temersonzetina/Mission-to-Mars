#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up your path and the URL for scraping.
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Create a function to run/rerun this code as needed.
def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Set up HTML parser.
    html = browser.html
    news_soup = soup(html, 'html.parser')
    slide_elem = news_soup.select_one('div.list_text')

    try:
        # Begin scraping by looking for content title (title of the article).
        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first 'a' tag and save it as the news title.
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
   
    except AttributeError:
         return None, None

    # Print the news_title and news_p.
    return news_title, news_p

# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Define a function to run this code regularly.
def featured_image(browser):

    # Find and click the full size image button.
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup.
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Find the relative - or latest - image URL
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    except AttributeError:
        return None

    # Add the base URL, so that you're able to access the full link.
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

    # Define the function to return a table.
def mars_facts():
    try: 
        # Use read_html to scrape the facts into a dataframe. 
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None

    # Assign columns and set index for dataframe.
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    # Convert dataframe into HTML object, using bootstrap.
    return df.to_html()

    browser.quit()




