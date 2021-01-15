from collections import Counter
from operator import itemgetter

from models import fieldnames
from kbimport import load_records
from reporting import write_report


def find_duplicates(records):
    duplicate_titles = _find_duplicate_titles(records)
    duplicate_articles = _collect_duplicate_articles(records, duplicate_titles)
    return duplicate_articles


def _find_duplicate_titles(records):
    print(f'Detecting duplicates.')
    titles = [record[fieldnames.title] for record in records]
    title_counts = Counter(titles)
    duplicate_titles = [
        title for (title, count) in title_counts.most_common()
        if count > 1
    ]
    print(f'Found {len(duplicate_titles)} duplicates.')
    return duplicate_titles


def _collect_duplicate_articles(records, duplicate_titles):
    print('Collecting duplicate articles.')
    duplicate_articles = [
        article for article in records
        if article[fieldnames.title] in duplicate_titles
    ]
    print('Sorting duplicate articles.')
    duplicate_articles.sort(key=itemgetter(fieldnames.title))
    return duplicate_articles
