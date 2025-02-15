import sys

args = sys.argv[1::]

srt = False
data_dict = {}

for val in args:
    if '--sort' not in val:
        val = val.split('=')
        data_dict[val[0]] = val[1]
    else:
        srt = True

data_dict = {k: v for k, v in sorted(data_dict.items())} if srt else data_dict

for key, val in data_dict.items():
    print(f'Key: {key} Value: {val}')
