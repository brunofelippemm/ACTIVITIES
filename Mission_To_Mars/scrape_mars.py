# Imports
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pymongo
import re

conn = 'mongodb://localhost:27017'

def scrapeMars():

    # Set up Splinter
    executable_path = {'executable_path': 'chromedriver.exe'}

    with Browser('chrome', **executable_path, headless=False) as browser:

        # # Collect the latest News Title and Paragraph Text
        url = f"https://mars.nasa.gov/news/"
        browser.visit(url)
        soup = bs(browser.html, 'html.parser')

        # Store title and paragraph into variables
        news_title = soup.find("div", class_="content_title").text
        news_par = soup.find("div", class_="article_teaser_body").text


        # Visit the JPL site
        jpl_url = f"https://www.jpl.nasa.gov"
        mars_images_paths = "/spaceimages/?search=&category=Mars"
        browser.visit(jpl_url + mars_images_paths)
        soup = bs(browser.html, 'html.parser')

        # Find the element which hold the featured image path and select the proper attribute for the link
        feat_img_path = soup.find("a", class_="button fancybox")['data-fancybox-href']
        feat_img_fullpath = jpl_url + feat_img_path


        # Mars Weather
        mw_twitter_url = f"https://twitter.com/marswxreport?lang=en"
        browser.visit(mw_twitter_url)
        soup = bs(browser.html, 'html.parser')
        mars_weather = soup.find('p', 
                         class_ ='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text', 
                         string=re.compile("InSight")).text
                         
        # Mars Facts
        mars_facts_url = f"https://space-facts.com/mars/"
        # Read HTML table with pandas
        mars_facts_df =  pd.read_html(mars_facts_url)[1]
        mars_facts_df.columns = ["Description", "Value"]
        mars_facts_df.set_index("Description", inplace = True)


        # Mars Hemispheres
        usgsAstro_url = f"https://astrogeology.usgs.gov"
        search_url = f"/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        full_url = usgsAstro_url + search_url

        hemi_images = []
        browser.visit(full_url)
        soup = bs(browser.html, 'html.parser')

        # Find and store the images
        hemi_links = soup.find_all("div", class_="description")
        for link in hemi_links:
            hemi_url = usgsAstro_url + link.a["href"]
            browser.visit(hemi_url)
            soup = bs(browser.html, 'html.parser')
            image = usgsAstro_url + soup.find("img", class_="wide-image")["src"]
            title = soup.find("h2", class_="title").text.replace(" Enhanced", "")
            hemi_images.append( { "title" : title, "img_url" : image } )


    data = {"newsTitle" : news_title,
    "newsDescription" : news_par,
    "featuredImageUrl" : feat_img_fullpath,
    "marsWeather" : mars_weather,
    "marsFacts" : mars_facts_df.to_dict(),
    "imageList" : hemi_images}

    return data


def storeInDb(data):
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.Mars
    db.MarsData.drop()
    db.MarsData.insert(data)
    client.close()


def getData():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.Mars
    collection = db.MarsData
    data = collection.find_one()
    return data