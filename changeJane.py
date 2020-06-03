#!/usr/bin/env python3

import sys
import subprocess

f = open(sys.argv[1])
for i in f.readlines():
    i = i.strip()
    b = i.replace("jane", "jdoe")
    subprocess.run(["mv", i, b])
f.close()
