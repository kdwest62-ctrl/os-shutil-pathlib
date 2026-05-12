import shutil
from pathlib import Path

try:
    path = Path(input("Directory path: "))
    if path.exists():
        def convert(num, unit_choice):
            if unit_choice == 'kb':
                result = num / 1024
                return round(result, 2)
            elif unit_choice == 'mb':
                result = num / (1024**2)
                return round(result, 2)
            elif unit_choice == 'gb':
                result = num / (1024**3)
                return round(result, 2)
        def percent(part, whole):
            result = (part / whole) * 100
            return round(result, 2)

        files = []
        for item in path.rglob('*'):
            if item.is_file():
                files.append(item)

        if len(files) > 0:
            unit = input("Select unit (kb, mb, gb): ")
            usage = shutil.disk_usage(path)
            total = convert(usage.total, unit)
            used = convert(usage.used, unit)
            free = convert(usage.free, unit)
            percent_used = percent(used, total)
            percent_free = percent(free, total)
            print(f"Total space: {total} {unit}")
            print(f"Used space: {used} {unit} [{percent_used}%]")
            print(f"Free space: {free} {unit} [{percent_free}%]")
            print("-" * 8)
            total_size = 0
            for file in files:
                size = convert(file.stat().st_size, unit)
                total_size += size
                print(f"{size} {unit} | {file}")
            print(f"Directory size: {round(total_size, 2)} {unit}")
            percent_dir = percent(total_size, total)
            print(f"Disk space occupied by directory: {percent_dir}%")
        else:
            print("No files in directory")
    else:
        print("Path not found")
except TypeError:
    print("Unit not found")
