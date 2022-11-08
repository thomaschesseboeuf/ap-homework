def scan(str, extent):
    from datetime import datetime as dt
    from pathlib import Path
    p = Path(str)
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