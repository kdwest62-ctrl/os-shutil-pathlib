from pathlib import Path

path = Path(input("Directory path: "))
if path.exists():
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

    files = []
    for item in path.rglob('*'):
        if item.is_file():
            files.append(item)
    if len(files) > 0:
        unit = input("Select unit (kb, mb, gb): ")
        min_size = float(input(f"Minimum file size ({unit}): "))
        match = []
        sizes = []
        for file in files:
            size = convert(file.stat().st_size, unit)
            if size >= min_size:
                match.append(file)
                sizes.append(size)

        if len(match) > 0:
            match_reference = dict(zip(match, sizes))
            for k, v in match_reference.items():
                print(f"{v} {unit} | {k}")
            remove = input("Remove all files or selection (a/s): ")
            if remove == 'a':
                for item in match:
                    item.unlink()
                    print(f"{item} removed successfully")
            elif remove == 's':
                total = int(input("How many files to remove? "))
                if 0 < total <= len(match):
                    nums = [i for i in range(len(match))]
                    reference = dict(zip(nums, match))
                    for index, file in reference.items():
                        print(index, file)
                    count = 0
                    while count < total:
                        select = int(input("Select file (number): "))
                        if select in reference.keys():
                            reference[select].unlink()
                            print(f"{reference[select]} removed successfully")
                            count += 1
                        else:
                            print("Number not in list")
        else:
            print("No files matched the criteria")
    else:
        print("Empty directory")
else:
    print("Path does not exist")
