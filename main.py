from kbimport import load_records
from duplicates import find_duplicates, get_excess_ids
from snow_query import get_snow_query
from reporting import write_report, write_to_file


def main():
    print('Starting scan.')
    records = load_records('./kb_export')
    duplicate_articles = find_duplicates(records)
    excess_ids = get_excess_ids(duplicate_articles)
    snow_query = get_snow_query(excess_ids)
    write_to_file(snow_query, './report/snow_query.txt')
    write_report(duplicate_articles, './report/report.csv')
    print('Done.')


if __name__ == '__main__':
    main()
