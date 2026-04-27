import shutil
from pathlib import Path

try:
    src_path = Path(input("Source directory path: "))
    if src_path.exists():
        def get_filename(path):
            file_names = []
            for item in path.iterdir():
                if item.is_file():
                    file_names.append(item.name)
            return file_names
        def sync(files, path):
            for item in path.iterdir():
                item.unlink()
            for file in files:
                shutil.copy2(file, path)

        src_file_names = get_filename(src_path)
        if len(src_file_names) > 0:
            total = int(input("Number of directories to sync with source: "))
            if total > 0:
                count = 0
                while count < total:
                    dir_path = Path(input(f"Directory path: "))
                    if dir_path.exists():
                        dir_file_names = get_filename(dir_path)
                        if dir_file_names == src_file_names:
                            print("Files in directory already synced with source")
                            count += 1
                        else:
                            src_files = [item for item in src_path.iterdir() if item.is_file()]
                            sync(src_files, dir_path)
                            print("Success! Files synced")
                            count += 1
                    else:
                        print("Path does not exist")
                        count += 1
        else:
            print("No files in source directory")
    else:
        print("Path does not exist")
except ValueError:
    print("Invalid input")
