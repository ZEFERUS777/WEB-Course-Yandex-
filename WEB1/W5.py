import json
import sys


def read_json(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)


inp = read_json('scoring.json')["scoring"]
test_points = {}

for group in inp:
    points = group['points']
    tests = group['required_tests']
    points_per_test = points / len(tests)

    for test_number in tests:
        test_points[test_number] = points_per_test

verdicts = [line.strip() for line in sys.stdin]

total = 0
for test_number in test_points:
    index = test_number - 1

    if index < len(verdicts) and verdicts[index] == 'ok':
        total += test_points[test_number]

print(int(total))
