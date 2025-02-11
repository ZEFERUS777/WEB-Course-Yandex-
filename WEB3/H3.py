import argparse


def count_lines(filename: str) -> int:
    try:
        with open(filename, 'r') as file:
            return len(file.readlines())
    except Exception:
        return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    lk = parser.parse_args()
    print(count_lines(lk.file))


if __name__ == "__main__":
    main()
