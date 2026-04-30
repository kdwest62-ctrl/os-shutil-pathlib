import shutil
from pathlib import Path

try:
    path = Path(input("Input path (check for directories): "))
    if path.exists():
        dirs = []
        dir_names = []
        for item in path.iterdir():
            if item.is_dir():
                dirs.append(item)
                dir_names.append(item.name)

        if len(dirs) > 0:
            print(dir_names)
            decide = input("Archive all directories or select from menu (a/s): ")
            if decide == "a":
                names = []
                for item in dir_names:
                    archive_name = input(f"Archive name for {item}: ")
                    if archive_name not in names:
                        names.append(archive_name)
                        dst_path = Path(input("Destination path: "))
                        if dst_path.exists():
                            dst = str(dst_path / archive_name)
                            src = str(path / item)
                            shutil.make_archive(dst, "zip", src)
                            print(f"{Path(item).name} archived as {archive_name}")
                        else:
                            print("Destination path does not exist")
                            print("Directory not archived")
                    else:
                        print("Archive name already exists")
                        print("Directory not archived")
            elif decide == "s":
                total = int(input("Number of directories to archive: "))
                if 0 < total < len(dirs):
                    count = 1
                    while count <= total:
                        names = []
                        dir_name = input(f"Directory {count} name: ")
                        if dir_name in dir_names:
                            archive_name = input(f"Archive name for {dir_name}: ")
                            if archive_name not in names:
                                dst_path = Path(input("Destination path: "))
                                if dst_path.exists():
                                    dst = str(dst_path / archive_name)
                                    src = str(path / dir_name)
                                    shutil.make_archive(dst, "zip", src)
                                    print(f"{dir_name} archived as {archive_name}")
                                    count += 1
                                else:
                                    print("Destination path does not exist")
                            else:
                                print("Archive name already exists")
                        else:
                            print("Directory not found")
        else:
            print("No directories found")
    else:
        print("Path does not exist")
except ValueError:
    print("Invalid input")
