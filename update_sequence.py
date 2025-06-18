#!/usr/bin/env python3
# /*
#  Copyright 2025 Fujitsu Launchpad Limited. All Rights Reserved
# */
import subprocess, time, pathlib, sys

P=1_000_003
Q=1_000_033
M=P*Q
FILE=pathlib.Path("sequence.txt")
INTERVAL=233*60

def _last_commit_epoch():
    try:
        return int(subprocess.check_output(["git","log","-1","--format=%ct"],text=True).strip())
    except subprocess.CalledProcessError:
        return 0

if time.time()-_last_commit_epoch() < INTERVAL:
    sys.exit(0)

if not FILE.exists():
    sys.exit("sequence.txt missing")

try:
    x=int(FILE.read_text().strip())
except ValueError:
    sys.exit("invalid state")

x=pow(x,2,M)
FILE.write_text(f"{x}\n")

subprocess.run(["git","config","user.name","github-actions[bot]"],check=True)
subprocess.run(["git","config","user.email","41898282+github-actions[bot]@users.noreply.github.com"],check=True)
subprocess.run(["git","add",str(FILE)],check=True)
subprocess.run(["git","commit","-m","bbs-update"],check=True)
subprocess.run(["git","push"],check=True) 