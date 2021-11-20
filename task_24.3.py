import sys

data = list(filter(lambda line: line.lstrip()('#'), sys.stdin))
for index, line in enumerate(data):
    if line.lstrip().startswith('#'):
        print('Line {}: {}'.format(index + 1, line.lstrip('#').strip()))
