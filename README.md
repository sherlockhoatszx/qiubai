## Introduction
Here is a crawler demo excuted by 'Scrapy'. It crawl the website of 'qiushibaike',which is a joke collection web in china.

##Items
include:
author
content
comment

##Database
Mongodb, a 'key-value'database.

##How to run 
switch dictionary to qiubai as your current dictionary in your terms.'cd /qiubai'
and type in :scrapy crawl qiubai to run the code. After the crawler finished its work, run 'python serviceFlask.py' , and open the http address in your browser, then you can see the crawled results.





