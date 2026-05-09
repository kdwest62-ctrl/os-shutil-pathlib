from pathlib import Path
import shutil

path = Path(input("Directory path: "))
if path.exists():
    files = []
    for item in path.rglob('*'):
        if item.is_file():
            files.append(item)

    if len(files) > 0:
        backup_list = []
        print("1. Show backup list\n2. Add files\n3. Remove files\n4. Backup\n5. Exit")
        while True:
            choice = input("Select task (num): ")
            if choice == '1':
                if len(backup_list) == 0:
                    print("No files in backup list")
                else:
                    for item in backup_list:
                        print(item)
            elif choice == '2':
                nums = [i for i in range(len(files))]
                reference = dict(zip(nums, files))
                for k, v in reference.items():
                    print(k, v)
                total = int(input("How many files to add? "))
                count = 0
                while count < total:
                    number = int(input("Select file (input number): "))
                    backup_list.append(reference[number])
                    print(f"{reference[number]} added to list")
                    count += 1
            elif choice == '3':
                if len(backup_list) == 0:
                    print("No files in backup list")
                else:
                    print(backup_list)
                    total = int(input("How many files to remove? "))
                    nums = [i for i in range(len(backup_list))]
                    reference = dict(zip(nums, backup_list))
                    for k, v in reference.items():
                        print(k, v)
                    count = 0
                    while count < total:
                        number = int(input("Select file (num): "))
                        del backup_list[number]
                        print(f"{reference[number]} removed from list")
                        count += 1
            elif choice == '4':
                if len(backup_list) == 0:
                    print("No files in backup list")
                else:
                    decide = input("Create new directory or use existing (c/u): ")
                    if decide == 'c':
                        location = Path(input("Location: "))
                        name = input("Name: ")
                        dir_path = location / name
                        dir_path.mkdir()
                        for item in backup_list:
                            shutil.copy2(str(item), str(dir_path))
                            print(f"{item} copied to {dir_path}")
                    elif decide == 'u':
                        dir_path = Path(input("Directory path: "))
                        if dir_path.exists():
                            for item in backup_list:
                                shutil.copy2(str(item), str(dir_path))
                                print(f"{item} copied to {dir_path}")
                        else:
                            print("Path does not exist")
            elif choice == '5':
                break
            else:
                print("Option not available")
    else:
        print("No files in directory")
else:
    print("Path does not exist")
