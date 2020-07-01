# Ecom-Scraper / E-Commerce Frameworks Scraper

Identifying E-Commerce Frameworks from popular romanian web stores.

The scraper will grab the top romanian e-commerce websites according to [trafic.ro](http://trafic.ro) and will clusterize them by the CMS they are built on.

-----------------------------------

Usage:

1. Install scrapy.

2. Generate a What CMS API key by going to the [WhatCMS API page](https://whatcms.org/APIKey). 
   Put the key in `ecommerce/ecommerce/spiders/getframework.py`.

3. Run the Scrapy spider. It will output a .txt file containing info about nuclear test sites.
    ```
    scrapy crawl getframework
    ```

4. It will output a .txt file containing the number of websites for each known CMS:
    ```
    {"null": 111, "PrestaShop": 6, "OpenCart": 15, "WordPress": 6, "Magento": 5, "Drupal": 1, "Liferay": 1, "Joomla": 2, "PHP-Nuke": 1, "osCommerce": 5, "CMS Made Simple": 1, "BigCommerce": 1, "Blogger": 5, "Adobe Dreamweaver": 1}
    ```

5. It will also output to console the market share of each known CMS based of the data above:
    ```
    Unknown -> 68.94%
    PrestaShop -> 3.73%
    OpenCart -> 9.32%
    WordPress -> 3.73%
    Magento -> 3.11%
    Drupal -> 0.62%
    Liferay -> 0.62%
    Joomla -> 1.24%
    PHP-Nuke -> 0.62%
    osCommerce -> 3.11%
    CMS Made Simple -> 0.62%
    BigCommerce -> 0.62%
    Blogger -> 3.11%
    Adobe Dreamweaver -> 0.62%
    ```

    
## Current status

This works mediocre because of the poor selection of websites on trafic.ro. Most of the CMSs used by the websites are unknown because they are romanian and they are not popular worldwide. If there was a similar datasource available (all CMSs in one place) it would have been more conclusive and useful.

Thanks to Trafic.ro.