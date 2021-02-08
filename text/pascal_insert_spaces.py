#!/usr/bin/python3

import sys

for pascal in sys.stdin:
    with_spaces = []
    for c in pascal.rstrip():
        if c.isupper():
            with_spaces.append(' ')
        with_spaces.append(c)
    print(''.join(with_spaces[1:]))
