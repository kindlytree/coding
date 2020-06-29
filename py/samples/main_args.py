#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse

if __name__ == "__main__":
    p = argparse.ArgumentParser(description = 'For function use')
    p.add_argument('Intergers',help = 'one or more intergers is need',nargs = '+',metavar = 'N',type = int)
    p.add_argument('-x',help = 'test self-function',type = func)
    args = p.parse_args()
    print(args.x(args.Intergers))