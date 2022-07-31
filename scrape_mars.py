# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd
from time import sleep

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    # create mars_data dict that we can insert into mongo
    mars_data = {}
    # In[2]:


    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


    # In[3]:


    # Retrieve page with the requests module
    response = requests.get(url)


    # In[4]:


    #Print response text
    response.text


    # In[5]:


    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')


    # In[6]:


    # Examine the results via prettyify, then determine element that contains News Title and Paragraph Text.
    print(soup.prettify())


    # In[7]:


    # Extract the title of the HTML document
    soup.title


    # In[8]:


    # Extract the text of the title
    soup.title.text


    # In[9]:


    # Clean up the text and assign it to a variable that can be called later
    news_title = soup.title.text.strip()


    # In[10]:


    # Print title variable
    news_title


    # In[11]:


    # Extract the contents of the HTML body
    soup.body


    # In[12]:


    # Extract the text of the body
    soup.body.text


    # In[13]:


    # Extract all paragraph elements
    soup.body.find_all('p')


    # In[14]:


    # Text of the first paragraph
    soup.body.p.text


    # In[15]:


    # Clean up the text and assign to a variable that can be called later
    news_p = soup.body.p.text.strip()


    # In[16]:


    # Print paragraph variable
    news_p


    # In[17]:


    # # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    # get_ipython().system('which chromedriver')


    # In[18]:


    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[19]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    # In[20]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    browser.click_link_by_partial_text('FULL IMAGE')
    sleep(60)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    browser.click_link_by_partial_text('more info')


    # In[21]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[22]:


    photo_full = soup.find('img', class_='main_image')['src']


    # In[23]:


    photo_full


    # In[24]:


    photo_full = "https://www.jpl.nasa.gov"+photo_full


    # In[25]:


    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)


    # In[26]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[27]:


    mars_weather_all = soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')


    # In[28]:


    mars_weather_all[8]


    # In[29]:


    mars_weather = mars_weather_all[8].text.strip()


    # In[30]:


    mars_weather


    # In[31]:


    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
    tables


    # In[32]:


    browser.quit()


    # In[33]:


    type(tables)


    # In[34]:


    df = tables[0]
    df.head()


    # In[35]:


    df = df.rename(columns={0: "Description", 1: "Value"})


    # In[36]:


    df.head()


    # In[37]:


    html_table = df.to_html()
    html_table


    # In[38]:


    # You can also save the table directly to a file.

    df.to_html('table.html')

    # OSX Users can run this to open the file in a browser, 
    # or you can manually find the file and open it in the browser
    # get_ipython().system('open table.html')


    # In[39]:


    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[40]:


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # In[41]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[42]:


    browser.click_link_by_partial_text('Cerberus')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    Cerberus_title = soup.title.text.strip()
    Cerberus_url = soup.find('a', target='_blank')['href']
    browser.back()

    browser.click_link_by_partial_text('Schiaparelli')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    Schiaparelli_title = soup.title.text.strip()
    Schiaparelli_url = soup.find('a', target='_blank')['href']
    browser.back()

    browser.click_link_by_partial_text('Syrtis Major')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    Syrtis_Major_title = soup.title.text.strip()
    Syrtis_Major_url = soup.find('a', target='_blank')['href']
    browser.back()

    browser.click_link_by_partial_text('Valles Marineris')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    Valles_Marineris_title = soup.title.text.strip()
    Valles_Marineris_url = soup.find('a', target='_blank')['href']


    # In[43]:


    browser.quit()


    # In[44]:


    Cerberus_url


    # In[45]:


    Cerberus_title


    # In[46]:


    Schiaparelli_url


    # In[47]:


    Schiaparelli_title


    # In[48]:


    Syrtis_Major_url


    # In[49]:


    Syrtis_Major_title


    # In[50]:


    Valles_Marineris_url


    # In[51]:


    Valles_Marineris_title


    # In[52]:


    hemisphere_image_urls = [
        {"title": f"{Valles_Marineris_title}", "img_url": f"{Valles_Marineris_url}"},
        {"title": f"{Cerberus_title}", "img_url": f"{Cerberus_url}"},
        {"title": f"{Schiaparelli_title}", "img_url": f"{Schiaparelli_url}"},
        {"title": f"{Syrtis_Major_title}", "img_url": f"{Syrtis_Major_url}"},
    ]

#     # create soup object from html
#     html = browser.html
#     report = BeautifulSoup(html, "html.parser")
#     mars_report = report.find_all("p")
#     # add it to our surf data dict
#     mars_data["report"] = build_report(mars_report)
#     # return our surf data dict

    browser.quit()
    return mars_data


# # # helper function to build surf report
# # def build_report(mars_report):
# #     final_report = ""
# #     for p in mars_report:
# #         final_report += " " + p.get_text()
# #         print(final_report)
# #     return final_report

    # The default port used by MongoDB is 27017
    # https://docs.mongodb.com/manual/reference/default-mongodb-port/
    conn = 'mongodb://localhost:27017'
    myclient = pymongo.MongoClient(conn)

    # Define the 'mars_app' database in Mongo
    # db = myclient[mars_app]

    # Insert a document into the 'mars' collection
    # db.mars.insert_one(hemisphere_image_urls)
    # mars.insert(hemisphere_image_urls)

    mydb = myclient["mars_app"]
    mycol = mydb["mars"]

    # mydict = { "name": "John", "address": "Highway 37" }

    x = mycol.insert_one(Cerberus_url)