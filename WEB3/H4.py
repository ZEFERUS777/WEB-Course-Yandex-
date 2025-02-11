import argparse
import sys


def copy_file(source: str, destination: str, upper: bool = False, lines: int = None):
    try:
        with open(source, 'r', encoding='utf-8') as source_file:
            if lines is not None:
                content = [source_file.readline() for _ in range(lines)]
            else:
                content = source_file.readlines()
        if upper:
            content = [line.upper() for line in content]
        with open(destination, 'w', encoding='utf-8') as destination_file:
            destination_file.writelines(content)

    except FileNotFoundError:
        print(f"Ошибка: Файл-источник '{source}' не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--upper', action='store_true')
    parser.add_argument('--lines', type=int)
    parser.add_argument('source', type=str)
    parser.add_argument('destination', type=str)

    args = parser.parse_args()

    copy_file(args.source, args.destination, args.upper, args.lines)


if __name__ == '__main__':
    main()
