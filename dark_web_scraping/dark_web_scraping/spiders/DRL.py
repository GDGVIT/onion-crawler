from collections import Counter
import lxml.html.clean
from string import punctuation

import scrapy
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
    # return dict(Counter(tokens))

    # TF-IDF
    word_counter = Counter(tokens)
    total_words = sum(word_counter.values())
    for key in word_counter:
        word_counter[key] = word_counter[key]/total_words
    return word_counter


class DrlSpider(scrapy.Spider):
    name = 'DRL'
    allowed_domains = ['onion']
    # start_urls = ['http://link6i54qxpk3ac7.onion/cat/1']
    start_urls = ['http://link6i54qxpk3ac7.onion/cat/9/page/{}'.format(page) for page in range(1, 5)]

    def parse(self, response):

        soup = BeautifulSoup(response.body, "html.parser")
        links = set()
        for link in soup.findAll('a'):
            inspect_link = link.get('href')
            if '.onion' in inspect_link:
                links.update({inspect_link})

        # Title
        title = cleanme(soup.title.text)

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
        print(dir(response))
        yield {
            'url': response.url,
            'title': title,
            'keywords': keywords,
            'description': description,
            'meta': response.meta,
            'links': links,
            'word_frequency': word_frequency
        }

        # next_pages = links

        # for next_page in next_pages:
        #     if next_page:
        #         yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse)