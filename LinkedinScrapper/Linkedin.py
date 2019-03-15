
# coding: utf-8

# In[151]:


import time
import numpy as np
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[152]:


browser = webdriver.Chrome()


# In[153]:


url = u'https://www.linkedin.com' #First we will need to login otherwise, if LinkedIn will automatically redirect to sign in page.
browser.get(url)


# In[154]:


# for entering Username
username = browser.find_element_by_class_name('login-email')
username.send_keys('adityak2920@gmail.com')

# for entering Password
password = browser.find_element_by_class_name('login-password')
password.send_keys('Tarakmehta')

# locating submit button and mimicing button click
log_in_button = browser.find_element_by_xpath('//*[@type="submit"]')
log_in_button.click()


# In[155]:


com_urls = ["https://www.linkedin.com/company/expertise-events",
"https://www.linkedin.com/company/jscstone",
"https://www.linkedin.com/company/exhibitions-&-trade-fairs",
"https://www.linkedin.com/company/penton-media-europe",
"https://www.linkedin.com/company/transworld-exhibits",
"https://www.linkedin.com/company/faitma",
"https://www.linkedin.com/company/motor-trend-auto-shows-inc",
"https://www.linkedin.com/company/show-group-enterprises-pty-limited",
"https://www.linkedin.com/company/golden-triangle-angelnet",
"https://www.linkedin.com/company/scoop-international",
"https://www.linkedin.com/company/iaapa",
"https://www.linkedin.com/company/thetoyassociation"]


# In[156]:


designation = ["Event Co-ordinator",
"marketing director",
"PR consultant",
"Event portfolio director",
"Marketing Manager",
"Event Manager",
"Marcom manager",
"Brand Marketing Manager",
"Group Marketing Manager",
"Digital Marketing Manager",
"Brand Director",
"Project Manager",
"Senior marketing manager"]


# In[157]:


con_cap=pd.DataFrame([], columns=['Company name', 'Linkedin company URL', 'Employee first name', 'Employee Last name', 'profile Url', 'Designation', 'location'])


# In[158]:


for curl in com_urls:
    c_url = curl+"/people"
    browser.get(c_url)
    time.sleep(1)
    body= browser.find_element_by_tag_name('body')
    for _ in range(50):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
    html_source=browser.page_source
    sourcedata= html_source.encode('utf-8')
    soup=bs(sourcedata, 'html.parser')    
    emp_des = soup.body.find_all(class_="lt-line-clamp lt-line-clamp--multi-line ember-view") # emp designation
    prof_url = soup.body.find_all('a', class_="link-without-visited-state ember-view")# profile urls
    emp_name = soup.body.find_all(class_="org-people-profile-card__profile-title t-black lt-line-clamp lt-line-clamp--single-line ember-view")# emp_name
    com_loc = soup.body.find_all(class_="org-top-card-summary__info-item org-top-card-summary__headquarter")# company location
    com_name = soup.body.find_all(class_="org-top-card-summary__title t-24 t-black truncate")# company name
    for i, emname in enumerate(emp_name):
        for desig in designation:
            if desig in emp_des[i].text.strip():                
                name = emname.text.strip().split()
                fname = name[0]
                lname = name[1]
                cname = com_name[0].text.strip()
                purl = url + prof_url[i].attrs["href"]
                locname = com_loc[0].text.strip()
                print(fname)
                data = {'Company name': cname, 
                        'Linkedin company URL':curl, 
                        'Employee first name':fname, 
                        'Employee Last name':lname, 
                        'profile Url':purl, 
                        'Designation':emp_des[i].text.strip(), 
                        'location':locname}
                con_cap = con_cap.append(data, ignore_index=True)


# In[159]:


pd.DataFrame.to_csv(con_cap,'/Users/adityakumar/Desktop/linkedin.csv')


# # Technical Improvements:

# On the coding front, this can be improved because here I am searching exact words for designation as you have wrote in you message on linkedin. So, by changing keywords and by some other ways we can make our code more robust.

# # Ending Notes:
# 

# I can improve this a lot but due to lack of time beacuse my exams are going on. So, to do it less time, I have to use selenium with bs. Otherwise, I have used srapy which is better for large scale and I can implement this in scrapy. And for directly scraping linkedin after login, I have mailed LinkedIn for permission. So in some days, they are going to reply. After all of this, I just want to say that I can implement this in a better way, if I got this internship then I am going to make a pipeline for scraping such websites so that in simle steps one can scrape such websites.
