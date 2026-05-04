from pathlib import Path

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
        extension = input("Select files to rename (input extension): ")
        if extension in extensions:
            data = []
            for item in files:
                data.append(item.stat().st_mtime)

            reference = dict(zip(data, files))
            sorted_ref = dict(sorted(reference.items()))
            print("Format: new_name(counter)")
            new_name = input("new_name: ")
            count = 1
            for key in sorted_ref.keys():
                if sorted_ref[key].suffix == extension:
                    name_plus_num = new_name + str(count) + extension
                    sorted_ref[key].rename(path / name_plus_num)
                    print(f"{sorted_ref[key].name} renamed to {new_name}{count}")
                    count += 1
        else:
            print("Extension not found")
    else:
        print("No files in directory")
else:
    print("Path does not exist")
