import os
import subprocess


def edit(args):
    if os.geteuid() != 0:
        print("gitx edit requires root privileges.")
    else:
        subprocess.run(["sudo", "nano", "/usr/share/gitx/settings.py"])
