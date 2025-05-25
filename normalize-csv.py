#!/usr/bin/env python3

import sys

for line in open(sys.argv[1], "r").readlines():
    if line.count(',') > 2:
        columns = line.rstrip().split(",")
        key = columns[0]
        value = ";".join(columns[1:-1])
        set_by = columns[-1]
        print(f"{key},{value},{set_by} (value commas replaced with semicolons)")
    else:
        print(line.rstrip())
