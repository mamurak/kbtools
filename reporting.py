from csv import DictWriter

from formatting import remove_html_tags
from models import fieldnames


def write_report(articles, report_file_name):
    cleaned_articles = remove_html_tags(articles)
    print(f'Writing report to {report_file_name}.')
    with open(report_file_name, 'w') as outputfile:
        writer = DictWriter(
            outputfile, fieldnames=fieldnames.tolist, extrasaction='ignore'
        )
        writer.writeheader()
        writer.writerows(cleaned_articles)

    print('Wrote report.')
    return


def write_to_file(content, location):
    print(f'Writing {len(content)} characters to {location}.')
    with open(location, 'w') as outputfile:
        outputfile.write(content)
