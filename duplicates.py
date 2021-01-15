from collections import Counter
from operator import itemgetter

from models import fieldnames
from kbimport import load_records
from reporting import write_report


def main():
    print('Starting scan.')
    records = load_records('./kb_export')
    duplicate_articles = find_duplicates(records)
    write_report(duplicate_articles, './report/report.csv')
    print('Done.')


def find_duplicates(records):
    duplicate_titles = find_duplicate_titles(records)
    duplicate_articles = collect_duplicate_articles(records, duplicate_titles)
    return duplicate_articles


def find_duplicate_titles(records):
    print(f'Detecting duplicates.')
    titles = [record[fieldnames.title] for record in records]
    title_counts = Counter(titles)
    duplicate_titles = [
        title for (title, count) in title_counts.most_common()
        if count > 1
    ]
    print(f'Found {len(duplicate_titles)} duplicates.')
    return duplicate_titles


def collect_duplicate_articles(records, duplicate_titles):
    print('Collecting duplicate articles.')
    duplicate_articles = [
        article for article in records
        if article[fieldnames.title] in duplicate_titles
    ]
    print('Sorting duplicate articles.')
    duplicate_articles.sort(key=itemgetter(fieldnames.title))
    return duplicate_articles


if __name__ == '__main__':
    main()
