import argparse

parser = argparse.ArgumentParser()
parser.add_argument(dest='l', nargs='*')
args = parser.parse_args()

try:

    if len(args.l) <= 0:
        print('NO PARAMS')
    elif len(args.l) < 2:
        print('TOO FEW PARAMS')
    elif len(args.l) > 2:
        print('TOO MANY PARAMS')
    else:
        print(int(args.l[0]) + int(args.l[1]))
except Exception as e:
    print(type(e).__name__)
