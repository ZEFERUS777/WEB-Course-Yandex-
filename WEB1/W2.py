import zipfile
import os


def print_structure(zip_file, indent=0):
    for item in zip_file.namelist():
        if item.endswith('/'):
            continue

        parts = item.split('/')

        for i, part in enumerate(parts):
            if part:
                print('  ' * (indent + i) + part)
        if not item.endswith('/'):
            print('  ' * (indent + len(parts) - 1) + os.path.basename(item))


def main():
    archive_name = 'input.zip'
    with zipfile.ZipFile(archive_name, 'r') as zip_file:
        print_structure(zip_file)


if __name__ == "__main__":
    main()
