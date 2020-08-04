#!/usr/bin/python3

import sys

pascal = sys.argv[1]
with_spaces = []
for c in pascal:
    if c.isupper():
        with_spaces.append('_')
        with_spaces.append(c.lower())
    else:
        with_spaces.append(c)
print(''.join(with_spaces[1:]))
