import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
args = parser.parse_args()

if not args.arg:
    print("no args")
else:
    for item in args.arg:
        print(item)
