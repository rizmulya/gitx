from settings import usernames, auth_tokens, repo_name, branch_name, default_user
import subprocess
from datetime import datetime


def init(args):
    user_index = args.u if args.u is not None else default_user
    username = usernames[user_index]
    token = auth_tokens[user_index]

    branch = args.b or branch_name
    repo = args.r or repo_name

    subprocess.run(["rm", "-rf", ".git"]) if args.reinit else None
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", args.m])
    subprocess.run(["git", "branch", "-M", branch])
    subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{username}/{repo}.git"])
    
    push_command = ["git", "push", "-u", f"https://{token}@github.com/{username}/{repo}.git", branch]
    push_command.extend(["-f"]) if args.reinit else None
    
    subprocess.run(push_command)
