def scan(filename, extent):
    from datetime import datetime as dt
    from pathlib import Path
    p = Path(filename)
    if not (p.is_dir()):
        print('error, filename does not exist')
    TREE = list(p.glob("**/*" + extent))
    if len(TREE) == 0:
        print('no such file') 
    for file in TREE:
        print(file.absolute())
        date = dt.fromtimestamp( file.stat().st_mtime )
        print(f'{file.stat().st_size} B, last modified on {date}')
        with open(file) as f:
            line = f.readline()
        print(f'first line : {line}')
        
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', help = 'indiquer le chemin du dossier sous forme de filename')
parser.add_argument('extent', help = 'indiquer l extension sous forme de filename')
args = parser.parse_args()
filename = args.filename
extent = args.extent
scan(filename, extent)
