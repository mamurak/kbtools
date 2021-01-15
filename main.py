from kbimport import load_records
from reporting import write_report
from duplicates import find_duplicates


def main():
    print('Starting scan.')
    records = load_records('./kb_export')
    duplicate_articles = find_duplicates(records)
    write_report(duplicate_articles, './report/report.csv')
    print('Done.')


if __name__ == '__main__':
    main()
