import json
from pathlib import Path

out_json_path = 'updates.json'

combined = {}


for file in Path('.').glob('*.html'):
    with open(file, encoding='utf-8') as f:
        all_html = f.read()

    name = file.stem

    combined[name] = {
        'status': all_html
    }


with open(out_json_path, 'w', encoding="utf-8") as file:
    json.dump(combined, file)
