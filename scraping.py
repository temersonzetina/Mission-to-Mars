#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

# Define a new function to begin initializing browser 
def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    
    # Get news title and news paragraph from the browser.
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": mars_hemispheres(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data

# Create a function to run/rerun this code as needed.
def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first 'a' tag and save it as the news title.
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
   
    except AttributeError:
         return None, None

    # Print the news_title and news_p.
    return news_title, news_p

# ### Featured Images

# Define a function to run this code regularly.
def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

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
    return df.to_html(classes="table table-striped")

def mars_hemispheres(browser):

    # 1. Use browser to visit the URL
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Parse the resulting html with soup.
    html = browser.html
    img_soup = soup(html, 'html.parser')
    slide_elem = img_soup.select_one('div.list_text')

    #2. Create a list to hold the images and titles.
    hemisphere_image_urls = []
    hemisphere_image_urls

    # 3. Write code to retrieve the image urls and titles for each hemisphere.

    ### IMAGE 1 ###

    # Go to the sub-page for Image 1.
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    full_image_site = browser.find_by_tag('a')[4]
    full_image_site.click()
    # Parse the resulting html with soup.
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Scrape the image and title.
    img1_url_rel = img_soup.find('img', class_='wide-image').get('src')
    img1_url = f'https://marshemispheres.com/{img1_url_rel}'
    img1_title = img_soup.body.find('h2').text

    # Create dictionary
    hemisphere1 = {'img_url':img1_url, 'title':img1_title}
    hemisphere_image_urls.append(hemisphere1)
    hemisphere_image_urls

    ### IMAGE 2 ###

    # Go to the sub-page for Image 2.
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    full_image_site = browser.find_by_tag('a')[6]
    full_image_site.click()
    # Parse the resulting html with soup.
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Scrape the image and title.
    img2_url_rel = img_soup.find('img', class_='wide-image').get('src')
    img2_url = f'https://marshemispheres.com/{img2_url_rel}'
    img2_title = img_soup.body.find('h2').text

    # Create dictionary
    hemisphere2 = {'img_url':img2_url, 'title':img2_title}
    hemisphere_image_urls.append(hemisphere2)
    hemisphere_image_urls

    ### IMAGE 3 ###

    # Go to the sub-page for Image 3.
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    full_image_site = browser.find_by_tag('a')[8]
    full_image_site.click()
    # Parse the resulting html with soup.
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Scrape the image and title.
    img3_url_rel = img_soup.find('img', class_='wide-image').get('src')
    img3_url = f'https://marshemispheres.com/{img3_url_rel}'
    img3_title = img_soup.body.find('h2').text

    # Create dictionary
    hemisphere3 = {'img_url':img3_url, 'title':img3_title}
    hemisphere_image_urls.append(hemisphere3)
    hemisphere_image_urls

    ### IMAGE 4 ###

    # Go to the sub-page for Image 4.
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    full_image_site = browser.find_by_tag('a')[10]
    full_image_site.click()
    # Parse the resulting html with soup.
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Scrape the image and title.
    img4_url_rel = img_soup.find('img', class_='wide-image').get('src')
    img4_url = f'https://marshemispheres.com/{img4_url_rel}'
    img4_title = img_soup.body.find('h2').text

    # Create dictionary
    hemisphere4 = {'img_url':img4_url, 'title':img4_title}
    hemisphere_image_urls.append(hemisphere4)

    # Add dictionaries to URL list.
    hemisphere_image_urls = [hemisphere1, hemisphere2, hemisphere3, hemisphere4]

    # 4. Print dictionary items.
    return hemisphere_image_urls

# hemispheres = dict(hemisphere_image_urls)

if __name__ == "__main__":
    
    # If running as script, print scraped data
    print(scrape_all())


