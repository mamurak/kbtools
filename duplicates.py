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


def get_excess_ids(duplicate_articles):
    print(f'Extracting IDs of {len(duplicate_articles)} redundant articles.')
    excess_ids = []
    seen_titles = []
    for article in duplicate_articles:
        title = article[fieldnames.title]
        if title in seen_titles:
            article_id = article[fieldnames.id]
            excess_ids.append(article_id)
        else:
            seen_titles.append(title)
    print(f'Extracted {len(excess_ids)} excess IDs.')
    return excess_ids
