# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:33:32 2018

@author: Melvin, Daddy, Jado
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
 
my_url = 'https://www.bbc.com/sport'

#Getting the information from the url by downloading it into page_html variable 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parse the information into the html format ready to be processed
page_soup = soup(page_html,"html.parser")

#Giving the name of the output file where the output of the crawled data will be written
file_name = "F:\WebCrawler\FeaturesTextDownload6.txt"
f = open(file_name,"w")

#Crawl to get the link of the first page of sport column of bbc.com and then
#get into the link and get the whole text information from the link
num = 3
max_num = 13
links = []
while num < max_num:
    articles = page_soup.findAll("div",{"class":"gel-layout__item anfield__item anfield__item--"+str(num)+" gel-1/2@m gel-1/4@xxl"})
    num+=1

    for article in articles:
        short_link = article.article.a.get('href')
        ref = 'https://www.bbc.com'+short_link
        uClient1 = uReq(ref)
        page_html1 = uClient1.read()
        uClient1.close()
        page_soup1 = soup(page_html1,"html.parser")
        readings = page_soup1.findAll("div",{"id":"story-body"})
        data = readings[0].text.strip()
        f.write(data)
        links.append(ref)
        print(ref)

#Crawl into the first page to get into the links inside more news column of the first page 
#and retrieve the text information from the pages inside the column
print('----------------------------------------------')

addInfs = page_soup.findAll("div",{"class":"gel-layout__item velodrome__items"})
for addInf in addInfs:
    the_link = addInf.div.article.a.get('href')
    add_ref = 'https://www.bbc.com'+the_link
    uClient2 = uReq(add_ref)
    page_html2 = uClient2.read()
    uClient2.close()
    page_soup2 = soup(page_html2,"html.parser")
    readings = page_soup2.findAll("div",{"id":"story-body"})
    data = readings[0].text.strip()
    f.write(data)
    f.write('\n')
    print(add_ref)

#crawl into the "Features" column of the first page of the sport column of bbc.com to retrieve
#more information from the links inside the "Features" column
print('----------------------------------------------')

addInf2s = page_soup.findAll("div",{"class":"gel-layout__item gel-1/2@xs gel-1/3@m gel-1/4@l gel-1/3@xxl"})
for addInf2 in addInf2s:
    the_link2 = addInf2.article.a.get('href')
    add_ref2 = 'https://www.bbc.com'+the_link2
    uClient3 = uReq(add_ref2)
    page_html3 = uClient3.read()
    uClient3.close()
    page_soup3 = soup(page_html3,"html.parser")
    readings = page_soup3.findAll("div",{"id":"story-body"})
    data = readings[0].text.strip()
    f.write(data)
    f.write('\n')
    print(add_ref2)
    

#Crawl into the "All Sport" option and then get into the links of various sport categories
#After getting into the each sport categories, again, get into the "Features" column per 
#sport categories page to retrive text data from each pages of the links.
print('----------------------------------------------')

the_lis = page_soup.findAll("li",{"class":"primary-nav-flyout__item"})
for the_li in the_lis:
    link = the_li.a.get('href')
    full_link = 'https://www.bbc.com'+link
    uClient = uReq(full_link)
    page_html_part = uClient.read()
    uClient.close()
    per_part = soup(page_html_part,"html.parser")
    per_part_features = per_part.findAll("div",{"class":"gel-layout__item velodrome__items"})
    for per_part_feature in per_part_features:
        get_link = per_part_feature.findAll("a")
        short_link = get_link[0].get('href')
        full_link = 'https://www.bbc.com'+short_link
        uClient2 = uReq(full_link)
        page_html_source = uClient2.read()
        uClient2.close()
        another_page_soup = soup(page_html_source,"html.parser")
        readings = another_page_soup.findAll("div",{"id":"story-body"})
        data = readings[0].text.strip()
        f.write(data)
        f.write('\n')
        print(full_link)
    

f.close()