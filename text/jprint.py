#!/usr/bin/python3

from typing import Any
import json
import sys

def jprint(m: Any) -> None:
    print(json.dumps(m, indent=4, default=str))


if __name__ == "__main__":
    for line in sys.stdin:
        jprint(eval(line))
