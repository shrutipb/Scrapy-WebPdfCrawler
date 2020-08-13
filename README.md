# Scrapy-WebPdfCrawler

Icici lombard Insurance Company Public Disclosures pdf crawler it crwals the pdfs of all quarters of every financial year
  url : https://www.icicilombard.com/about-us/public-disclosure

# Requirements
1) Python 3.7.8
2) Works on Windows and Linux  

# Install 

the quick way:
 
  pip install scrapy
  
  See the install section in the documentation at https://docs.scrapy.org/en/latest/intro/install.html for more details.
  
# Crawled Data

This project Crawls pdfs, It creates a folder name as icicilombard inside folder it creats another folder name as present financial year. inside that folder we will get every quarter pdf's

# spiders
 $ scrapy
 
 This project contains one spider : icicilombard
 
 spider crawls the pdfs from same website https://www.icicilombard.com/about-us/public-disclosure
 
 You can learn more about the spiders by going through the Scrapy Tutorial https://docs.scrapy.org/en/latest/intro/tutorial.html
 
# Running the spiders

  You can run a spider using the scrapy crawl command, such as:
     
       scrapy crawl icici
