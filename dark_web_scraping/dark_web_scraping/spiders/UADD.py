from collections import Counter
import lxml.html.clean
from string import punctuation
import os
import logging

dir_path = os.path.dirname(os.path.realpath(__file__))

import scrapy
from scrapy.utils.log import configure_logging
from nltk.corpus import stopwords
from nltk import PorterStemmer
from bs4 import BeautifulSoup

stemmer = PorterStemmer()


# GLOBALS
STOPS = set(stopwords.words("english"))

def cleanme(content):
    """
    input: A String
    return: A Word Count Dictionary 
    - Remove Tags
    - Special Character Free (\n, \r, \t, extra_space)
    - Remove Punctuations
    - Create Word List
    - Remove Stop words (English)
    - Use Steaming
    - Word Count | TF-IDF
    """
    # Remove Tags
    cleaner = lxml.html.clean.Cleaner(
        allow_tags=[''],
        remove_unknown_tags=False,
        style=True,
    )
    html = lxml.html.document_fromstring(content)
    html_clean = cleaner.clean_html(html)
    text = html_clean.text_content().strip()

    # Special Character Free
    text.lower()
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('  ', ' ')

    # Remove Punctuations
    text = text.translate(str.maketrans('', '', punctuation))

    # Create Word List
    word_list = text.split(' ')

    # Remove Stop words (English)
    filtered_words = [word for word in word_list if word not in STOPS]

    # Steaming
    tokens = [stemmer.stem(t) for t in filtered_words]

    # Word Count
    return dict(Counter(tokens))

    # TF-IDF
    # word_counter = Counter(tokens)
    # total_words = sum(word_counter.values())
    # for key in word_counter:
    #     word_counter[key] = word_counter[key]/total_words
    # return word_counter


class UaddSpider(scrapy.Spider):

    name = 'UADD'
    allowed_domains = ['onion']

    # You can fetch urls from your DB here
    start_urls = open("{}/spider_data/user_added_urls.txt".format(dir_path)).read().splitlines()    

    # Logging
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='UADD_LOGS.log',
        format='%(levelname)s %(asctime)s: %(message)s',
        level=logging.INFO
    )    

    def parse(self, response):

        soup = BeautifulSoup(response.body, "html.parser")
        links = set()
        try:
            for link in soup.findAll('a'):
                inspect_link = link.get('href')
                if '.onion' in inspect_link:
                    links.update({inspect_link})
        except:
            pass

        # Title
        title = soup.title.text
        title_keywords = cleanme(title)

        # Meta Keywords & Description
        meta_tags = soup.find_all('meta')

        for meta_tag in meta_tags:
            if meta_tag.get('name') in ['keywords', 'Keywords']:
                keywords =  cleanme(meta_tag.get('content'))
                break
            else:
                keywords = ''

        for meta_tag in meta_tags:
            if meta_tag.get('name') in ['description', 'Description']:
                description =  cleanme(meta_tag.get('content'))
                break
            else:
                description = ''

        word_frequency = cleanme(response.text)
        # print(dir(response))

        yield {
            'url': response.url,
            'title': title,
            'title_keywords': title_keywords,
            'keywords': keywords,
            'description': description,
            'meta': response.meta,
            'links': links,
            'word_frequency': word_frequency
        }

        # Recursion |  Change Depth Settings in Settings.py
        # next_pages = links

        # for next_page in next_pages:
        #     if next_page:
        #         yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse)