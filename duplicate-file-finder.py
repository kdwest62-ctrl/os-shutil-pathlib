from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

path = Path(input('Directory path: '))
if path.exists():
    files = []
    stems = []
    for item in path.rglob('*'):
        if item.is_file():
            files.append(item)
            stems.append(item.stem)

    stems_no_repeat = []
    for stem in stems:
        if stem not in stems_no_repeat:
            stems_no_repeat.append(stem)
    counts = []
    for stem in stems_no_repeat:
        count = stems.count(stem)
        counts.append(count)
    stem_counter = dict(zip(stems_no_repeat, counts))

    stems_with_dpl = []
    for stem in stem_counter.keys():
        if stem_counter[stem] > 1:
            stems_with_dpl.append(stem)
    duplicate_files = []
    for file in files:
        if file.stem in stems_with_dpl:
            duplicate_files.append(file)

    if len(duplicate_files) == 0:
        print('No duplicates found')
    else:
        parent = []
        name = []
        for path in duplicate_files:
            parent.append(path.parent)
            name.append(path.name)

        data = {'Parent':[i for i in parent], 'Name': [i for i in name]}
        df = pd.DataFrame(data)
        print(df.to_string())
        print('-' * 8)

        print('Tasks\n1. Remove files\n2. Show file size distribution\n3. Exit')
        while True:
            task = input('Select task: ')
            if task == '1':
                pass
            elif task == '2':
                duplicate_sizes = []
                for path in duplicate_files:
                    duplicate_sizes.append(path.stat().st_size)
                file_sizes = []
                for path in files:
                    file_sizes.append(path.stat().st_size)

                data = [sum(duplicate_sizes) / sum(file_sizes),
                        (sum(file_sizes) - sum(duplicate_sizes)) / sum(file_sizes)]
                categories = ['Files + Duplicates', 'Files Without Duplicates']
                custom_colors = ['red', 'silver']
                plt.pie(data, labels=categories, colors=custom_colors, autopct='%1.1f%%')
                plt.title('File Size Distribution in Directory')
                plt.show()
            elif task == '3':
                print('Program closed')
                break
else:
    print('Path does not exist')
