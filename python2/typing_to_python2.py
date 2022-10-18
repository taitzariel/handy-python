#!/usr/bin/env python3

# simple - will not work for more complicated signatures

import sys

line = sys.stdin.read()

if 'def ' in line:
    line2, out_type = line.rsplit(' -> ')
    leading_space, line3 = line2.split('def ')
    method_name, args = line3.split('(')
    arg_names = []
    arg_types = []
    for arg in args.split(')')[0].split(', '):
        if ': ' in arg:
            arg_name, arg_type = arg.split(': ')
            if ' = ' in arg_type:
                arg_type, default = arg_type.split(' = ')
                arg_names.append(f'{arg_name}={default}')
            else:
                arg_names.append(arg_name)
            arg_types.append(arg_type)
        else:
            arg_names.append(arg)
    arg_names_str = ', '.join(arg_names)
    arg_types_str = ', '.join(arg_types)
    print(f'{leading_space}def {method_name}({arg_names_str}):')
    print(f'{leading_space}    # type: ({arg_types_str}) -> {out_type.split(":")[0]}')
else:
    print(line)

