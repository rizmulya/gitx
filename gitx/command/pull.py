import subprocess


def pull(args):
    subprocess.run(["git", "fetch"])
    subprocess.run(["git", "status"])
    print("Sync ...")
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "status"])
