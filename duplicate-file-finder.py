from pathlib import Path

try:
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
                            if len(match) > 1:
                                for num, path in reference.items():
                                    print(num, path)
                                keep = int(input("Select file to keep (input number): "))
                                confirm = input("Confirm delete? (y/n): ")
                                if confirm == 'y':
                                    del reference[keep]
                                    for num in reference.keys():
                                        reference[num].unlink()
                                        print(f"{reference[num]} removed")
                            else:
                                print("Only 1 file found")
                                confirm = input("Confirm delete? (y/n): ")
                                if confirm == 'y':
                                    for path in match:
                                        path.unlink()
                                        print(f"{path} removed")
                        elif decide == 's':
                            total = int(input("How many files to remove? "))
                            if total > 0:
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
                            print("Invalid input")
            else:
                print("Directory empty")
        else:
            print("Path does not exist")
    else:
        print("File name length must be 3 words or longer")
except ValueError:
    print("Please input a number")
