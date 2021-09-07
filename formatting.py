from copy import deepcopy
import re

from models import fieldnames


def remove_html_tags(articles):
    print('Cleaning article body texts.')
    clean_articles = [
        cleaned(article) for article in articles
    ]
    return clean_articles


def cleaned(article):
    cleaned_article = deepcopy(article)
    cleaned_article[fieldnames.text] = cleanhtml(cleaned_article[fieldnames.text])
    return cleaned_article


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    return cleantext
