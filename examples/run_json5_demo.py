from api_json_cleaner import cleanse_and_parse
from pathlib import Path

p = Path(__file__).with_name('dirty_json5.json')
print(cleanse_and_parse(p.read_bytes()))
