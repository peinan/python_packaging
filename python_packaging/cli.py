#!/usr/bin/env python
# coding: utf-8
#
# Filename:   cli.py
# Author:     Peinan ZHANG
# Created at: 2018-06-24


def main():
    import sys
    from .core import add

    if len(sys.argv) == 3:
        x, y = map(int, sys.argv[1:])
        print(add(x, y))
    else:
        print('please specify 2 arguments', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
