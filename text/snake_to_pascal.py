#!/usr/bin/python3

import sys

snake = sys.stdin.read().strip()
print(snake.title().replace('_',''), end='')
