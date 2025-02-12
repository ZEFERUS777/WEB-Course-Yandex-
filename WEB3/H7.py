import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sort', action='store_true')
parser.add_argument(dest='dicts', nargs='*')
args = parser.parse_args()
output_dict = {}
for i in args.dicts:
    chapters = i.split('=')
    output_dict[chapters[0]] = chapters[1]

if args.sort:
    output_dict = {k: v for k, v in sorted(output_dict.items())}
for i in output_dict.keys():
    print(f'Key: {i}\t Value: {output_dict[i]}')
