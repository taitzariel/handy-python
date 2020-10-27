#!/usr/bin/python3

# converts camel case or pascal case to snake case
# e.g. halloThere -> hallo_there

import sys

pascal = sys.argv[1]
chars = [pascal[0].lower()]
for c in pascal[1:]:
    if c.isupper():
        chars.append('_')
        chars.append(c.lower())
    else:
        chars.append(c)
print(''.join(chars), end='')
