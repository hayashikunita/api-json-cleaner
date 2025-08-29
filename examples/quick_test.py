from api_json_cleaner import cleanse_and_parse, save_json
from pathlib import Path

here = Path(__file__).parent
raw = here.joinpath('dirty.json').read_bytes()
obj = cleanse_and_parse(raw)
print('Parsed:', obj)
save_json(obj, str(here / 'cleaned.json'), ensure_ascii=False, indent=2)
print('Saved to', here / 'cleaned.json')