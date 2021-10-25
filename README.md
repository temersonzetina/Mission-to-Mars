# Mission-to-Mars

### Purpose
In this repository, there is a series of files contributing to a Flask-rendered site that compiles information about ongoing Mars-related research. The files include -

<ul>
<li> Scraping.py, which includes a set of functions that scrape each of the image and text-related components and stores the data in MongoDB
<li> App.py, which initializes the scraping functions and prepares the scraped data to incorporate into the Flask-generated site
<li> Index.html, which renders the web page in Flask
</ul>

The major tools incorporated in these files include -

<ul>
<li> Splinter, which initializes an automated browser pointed towards a selection of websites about Mars
<li> Beautiful Soup, which creates a set of objects from which the script scrapes text and images
<li> MongoDB, which holds the image and text data
<li> Flask, which renders the website on a local server
</ul>
