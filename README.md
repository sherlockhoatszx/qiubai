## Introduction
Here is a crawler demo excuted by 'Scrapy'. It crawls the website of 'qiushibaike',which is a joke collection web in china.

##Items defination:
include:
author
content
comment

##Database
Mongodb, a 'key-value'database.

##How to run 
1.type in 'mongo'in your terms to ensure the mongodatabase is in run

2.switch dictionary to qiubai as your current dictionary in your terms.'cd /qiubai'

3.type in :scrapy crawl qiubai to run the code. After the crawler finished its work, run 'python serviceFlask.py' 

4.open the http address in your browser, then you can see the crawled results.





