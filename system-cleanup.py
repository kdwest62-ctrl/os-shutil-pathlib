from pathlib import Path
import pandas as pd

def convert(num, unit_choice):
    if unit_choice == 'kb':
        result = num / 1024
        return round(result, 2)
    elif unit_choice == 'mb':
        result = num / (1024 ** 2)
        return round(result, 2)
    elif unit_choice == 'gb':
        result = num / (1024 ** 3)
        return round(result, 2)

path = Path(input('Directory path: '))
if path.exists():
    files = []
    for item in path.rglob('*'):
        if item.is_file():
            files.append(item)
    if len(files) > 0:
        unit = input('Select unit (kb, mb, gb): ')
        min_size = float(input(f'Minimum file size ({unit}): '))
        path = []
        name = []
        sizes = []
        total_size = []
        for file in files:
            size = convert(file.stat().st_size, unit)
            total_size.append(size)
            if size >= min_size:
                path.append(file)
                name.append(file.name)
                sizes.append(size)
        if len(name) > 0:
            print(f'Files: {len(files)}')
            print(f'Match: {len(name)}')
            data = {f'Size ({unit})': [i for i in sizes], 'Name': [i for i in name], 'Path': [i for i in path]}
            df = pd.DataFrame(data)
            print(df.to_string())
            print('-' * 8)

            print('Options')
            print('1. Histogram\n2. Pie chart\n3. Remove files\n4. Exit')
            print('-' * 8)
        else:
            print(f'Files: {len(files)}')
            print(f'Match: {len(name)}')
    else:
        print('Empty directory')
else:
    print('Path does not exist')
