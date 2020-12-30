from collections import Counter
from csv import DictWriter
from dataclasses import dataclass
import json
from operator import itemgetter
from pathlib import Path


@dataclass
class Fieldnames:
    title: str
    modification_date: str
    number: str
    text: str
    hyperlink: str

    @property
    def tolist(self):
        fieldnames = [
            self.title, 
            self.modification_date,
            self.number,
            self.text,
            self.hyperlink,
        ]
        return fieldnames


fieldnames = Fieldnames(
    title='short_description',
    modification_date='published',
    number='number',
    text='text',
    hyperlink='u_knowledge_permalink',
)


def main():
    print('Starting scan.')
    records = load_records('./kb_export')
    duplicate_articles = find_duplicates(records)
    write_report(duplicate_articles, './report/report.csv')
    print('Done.')


def load_records(kb_export_folder):
    print(f'Scanning folder {kb_export_folder}.')
    kb_export_path = Path(kb_export_folder)
    json_files = list(kb_export_path.glob('*.json'))
    print(f'Found JSON files in KB export folder: {json_files}')
    
    kb_export = json_files[0]
    print(f'Reading KB export file {kb_export.name}.')

    with open(kb_export, 'r') as inputfile:
        kb = json.load(inputfile)

    records = kb['records']
    print(f'Loaded KB with {len(records)} articles.')
    return records


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


def write_report(duplicate_articles, report_file_name):
    print(f'Writing report to {report_file_name}.')
    with open(report_file_name, 'w') as outputfile:
        writer = DictWriter(
            outputfile, fieldnames=fieldnames.tolist, extrasaction='ignore'
        )
        writer.writeheader()
        writer.writerows(duplicate_articles)

    print('Wrote report.')
    return


if __name__ == '__main__':
    main()
