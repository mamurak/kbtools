import json
from pathlib import Path


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
