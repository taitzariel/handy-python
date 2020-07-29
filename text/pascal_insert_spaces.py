#!/usr/bin/python3

import sys

pascal = sys.argv[1]
with_spaces = []
for c in pascal:
    if c.isupper(): # todo: ignore the first occurrence
        with_spaces.append(' ')
    with_spaces.append(c)
print(''.join(with_spaces))
