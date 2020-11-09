#!/usr/bin/env python
import sys
import os
file = sys.argv[1]
file_exe = file.split('.')[-2].replace('/', '')+'.exe'
os.system("mkdir -p .cache")
os.system(f"sed '1d' {file} > .cache/{file}")
os.system(f"cat .cache/{file}")
os.system(f"csc -out:.cache/{file_exe} .cache/{file}")
os.system(f"mono .cache/{file_exe}")
os.system("rm -rf .cache")
