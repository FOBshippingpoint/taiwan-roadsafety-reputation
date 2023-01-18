from pathlib import Path
import json

print('start: 1_clean_geojson')

data_path = Path('../data')

# Keep geometry and country NAME_ZHT, ADMO_A3 only
with open(data_path / 'original_countries.geo.json', 'r', encoding='utf-8') as f:
    geojson = json.load(f)

for f in geojson['features']:
    f['properties'] = {k:v for k,v in f['properties'].items() if k in ('NAME_ZHT', 'ADM0_A3')}

# 移除南極洲
geojson['features'] = [item for item in geojson['features'] if item['properties']['ADM0_A3'] not in ('ATA')]

with open(data_path / 'countries.geo.json', 'w', encoding='utf-8') as f:
    json.dump(geojson, f, indent=4, ensure_ascii=False)

print('done')
