from pathlib import Path

name = input("File name: ")
if len(name) >= 3:
    dir_path = Path(input("Search for files (input directory path): "))
    if dir_path.exists():
        files = []
        for item in dir_path.rglob('*'):
            if item.is_file():
                files.append(item)
        if len(files) > 0:
            match = []
            for file in files:
                if name in file.name:
                    match.append(file)
            if len(match) == 0:
                print("No files matched your search")
            else:
                for item in match:
                    print(item)
                remove = input("Remove files? (y/n): ")
                if remove == 'y':
                    nums = [i for i in range(len(match))]
                    reference = dict(zip(nums, match))
                    decide =  input("Remove all duplicates or a selection? (a/s): ")
                    if decide == 'a':
                        for num, path in reference.items():
                            print(num, path)
                        keep = int(input("Select file to be kept (input number): "))
                        del reference[keep]
                        for num in reference.keys():
                            reference[num].unlink()
                            print(f"{reference[num]} removed")
                    elif decide == 's':
                        total = int(input("How many files to remove? "))
                        for num, path in reference.items():
                            print(num, path)
                        count = 0
                        while count < total:
                            num = int(input("Remove file (input number): "))
                            if num in reference.keys():
                                reference[num].unlink()
                                print(f"{reference[num]} removed")
                                count += 1
                            else:
                                print("Number not in list")
        else:
            print("Directory empty")
    else:
        print("Path does not exist")
else:
    print("File name length must be 3 words or longer")
