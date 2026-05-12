from pathlib import Path

path = Path(input("Search for empty directories (input path): "))
if path.exists():
    dirs = []
    for item in path.rglob('*'):
        if item.is_dir():
            dirs.append(item)

    if len(dirs) > 0:
        empty_dirs = []
        for item in dirs:
            count = 0
            for i in item.iterdir():
                if i.is_file() or i.is_dir():
                    count += 1
            if count == 0:
                empty_dirs.append(item)
        if len(empty_dirs) > 0:
            for item in empty_dirs:
                print(item)
            remove = input("Remove all empty directories or selection? (a/s): ")
            if remove == 'a':
                for item in empty_dirs:
                    item.rmdir()
                    print(f"{item} removed successfully")
            elif remove == 's':
                nums = [n for n in range(len(empty_dirs))]
                reference = dict(zip(nums, empty_dirs))
                for num, empty_dir in reference.items():
                    print(num, empty_dir)
                total = int(input("How many empty directories to remove: "))
                if 0 < total <= len(empty_dirs):
                    removed = 0
                    while removed < total:
                        num = int(input("Select directory (number): "))
                        if num in reference.keys():
                            reference[num].rmdir()
                            removed += 1
                            print(f"{reference[num]} removed successfully")
                        else:
                            print("Number not in list")
                else:
                    print(f"There are {len(empty_dirs)} empty directories")
        else:
            print("No empty directories")
    else:
        print("No directories found in path")
else:
    print("Path does not exist")
