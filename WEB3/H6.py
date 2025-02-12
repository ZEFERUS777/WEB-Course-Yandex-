import argparse as arg

parser = arg.ArgumentParser()
parser.add_argument('--count', action='store_true')
parser.add_argument('--num', action='store_true')
parser.add_argument('--sort', action='store_true')
parser.add_argument('file', type=str)
args = parser.parse_args()

count = 0

try:
    with open(args.file, 'r', newline='\n') as f:
        content = f.readlines()
except Exception as e:
    print('ERROR')
    exit(1)

if args.sort:
    content = sorted(content)

for line in content:
    line = line.replace('\n', '').replace('\r', '')
    if args.num:
        print(f'{count} {line}')
    else:
        print(line)
    count += 1

if args.count:
    print(f'rows count: {count}')
