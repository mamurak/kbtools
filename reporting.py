from csv import DictWriter

from models import fieldnames


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


def write_to_file(content, location):
    print(f'Writing {len(content)} characters to {location}.')
    with open(location, 'w') as outputfile:
        outputfile.write(content)
