from pathlib import Path
import requests

SRC_URL = 'https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt'
DATA_DIR = Path('files', 'data')
DATA_DIR.mkdir(parents=True, exist_ok=True)
DEST_PATH = DATA_DIR.joinpath('global-temps-data.original.txt')

def fetch_and_save():
  resp = requests.get(SRC_URL)
  with open(DEST_PATH, 'w') as w:
    w.write(resp.text)
    return resp.text

if __name__ == '__main__':
  txt = fetch_and_save()
  print("Wrote", len(txt), 'chars to:', DEST_PATH)
