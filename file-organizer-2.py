import os
import shutil
from pathlib import Path

try:
    path = input("Directory path: ")
    if os.path.exists(path):
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

        items = os.listdir(path)
        if len(items) > 0:
            files = []
            sizes = []
            unit = input("Select unit (kb, mb, gb): ")
            if unit in ['kb', 'mb', 'gb']:
                for item in items:
                    file = os.path.join(path, item)
                    if os.path.isfile(file):
                        files.append(file)
                        sizes.append(convert(os.path.getsize(file), unit))
                files_with_sizes = dict(zip(sizes, files))

                total = int(input("Number of directories to create: "))
                if total > 0:
                    count = 1
                    while count <= total:
                        name = input(f"Directory {count} name: ")
                        min_size = float(input("Min file size (mb): "))
                        max_size = float(input("Max file size (mb): "))
                        if min_size > 0 and max_size > 0:
                            if max_size > min_size:
                                dir_path = os.path.join(path, name)
                                os.mkdir(dir_path)
                                for size, file in files_with_sizes.items():
                                    if min_size <= size <= max_size:
                                        shutil.move(file, dir_path)
                                        print(f"{Path(file).name} moved to {name}")
                                count += 1
                            else:
                                print("Max is always greater than min")
                        else:
                            print("File size cannot be 0 or lower")
            else:
                print("Unit not found")
        else:
            print("No files in path")
    else:
        print("Path not found")
except FileExistsError:
    print("Directory already exists")
except ValueError:
    print("Invalid input")
