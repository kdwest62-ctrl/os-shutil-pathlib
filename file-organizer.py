from pathlib import Path
import shutil

path = Path(input("Directory path: "))
if path.exists():
    files = []
    for item in path.iterdir():
        if item.is_file():
            files.append(item)

    if len(files) > 0:
        extensions = []
        for file in files:
            extensions.append(file.suffix)

        print(set(extensions))
        total = int(input("Number of file extensions to organize: "))
        if total > 0:
            count = 0
            while count < total:
                extension = input("Select extension: ")
                if extension in extensions:
                    decide = input("Create new directory or use existing (c/u): ")
                    if decide == 'c':
                        name = input("Directory name: ")
                        new_dir = path / name
                        Path(new_dir).mkdir()
                        for file in files:
                            if file.suffix == extension:
                                shutil.move(str(file), new_dir)
                                print(f"{file.name} moved to {name}")
                                count += 1
                    elif decide == 'u':
                        dir_names = []
                        for item in path.iterdir():
                            if item.is_dir():
                                dir_names.append(item.name)
                        print(dir_names)
                        name = input("Directory name: ")
                        if name in dir_names:
                            dir_path = path / name
                            for item in path.iterdir():
                                if item == dir_path:
                                    for file in files:
                                        if file.suffix == extension:
                                            shutil.move(str(file), dir_path)
                                            print(f"{file.name} moved to {name}")
                                            count += 1
                        else:
                            print("Directory not found")
                else:
                    print("File extension not found")
    else:
        print("No files in directory")
else:
    print("Path does not exist")
