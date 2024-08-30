#!/usr/bin/env python3

import sys
from pathlib import Path

lines = Path(sys.argv[1]).read_text().strip().split("\n")

while lines:
    (s, p, u, *lines) = lines
    path = p.split("=")[1].strip()
    url = u.split("=")[1].strip()
    if url.startswith("git@github.com:"):
        url = url[len("git@github.com:"):]
    elif url.startswith( "https://github.com/"):
        url = url[len("https://github.com/"):]
    else:
        print("unknown url " + url)
        exit(-1)

    print(f'<project remote="github" name="{url}" path="{path}" revision="master" />')
