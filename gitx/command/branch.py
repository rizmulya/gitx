import subprocess


def branch(args):
    subprocess.run(["git", "branch", args.b])
    subprocess.run(["git", "checkout", args.b])
    