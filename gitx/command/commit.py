import subprocess


def commit(args):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", args.m])
    