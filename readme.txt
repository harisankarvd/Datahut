Assignment for Data Analyst Internship @ Datahut
*********************************************
**********************************************
The "Batchwise_scrap.py" is used for batch-wise scraping approach and 
stored the data as pickle files in a folder called "data".

Then using "Yc_company.ipynb" and "Yc_funder.ipynb" extract all links 
and extract all Data Points to be Scrapped.

finally, "data_analysis.ipynb" ,cleaned the data and check
all values then convert to json file.

The scraped data json file present on the folder named "output" 
named with "output.json"


Methodology Used for Scraping:
*******************************
Asyncio: You utilized asyncio to handle asynchronous tasks concurrently, 
which improves the efficiency of web scraping by allowing multiple requests 
to be made simultaneously without blocking.

Beautiful Soup (BS4): You employed Beautiful Soup for parsing HTML and XML documents, 
enabling easy extraction of data from web pages.

Playwright: You utilized Playwright for browser automation, which allows interaction with 
JavaScript-heavy websites, rendering pages, and executing client-side scripts. 
This ensures comprehensive data retrieval, especially from dynamic websites.



Challenges Encountered and Solutions:
****************************************
Handling Dynamic Content: Dynamic content rendered by JavaScript could pose challenges. 
Utilizing Playwright helps overcome this by allowing interaction with dynamically generated elements.

Rate Limiting and IP Blocking: Websites might implement measures to prevent scraping, 
such as rate limiting or IP blocking. 
Implementing random user-agent headers and using proxies can help mitigate these issues.


Summary of Extracted Data:
***************************
Provide an overview of the data extracted, including the types of information collected, such as 

Company Information:
1. Name
2. Tagline
3. Description
4. Batch (e.g., W21 for Winter 2021)
5. Company type (Public, Private, etc.)
6. Industry tags (Marketplace, Health, FinTech, etc.)
7. Location (City, Country as listed on the page)
8. Website URL
9. Year founded
10.Team size
11.LinkedIn profile
12.Twitter handle
13.Facebook page
14.Crunchbase profile


Founder Information:
1. Name
2. Role within the company
3. Brief biography
4. LinkedIn profile
5. Twitter profile




Total no, data on json file is 4492



thannk you..............................