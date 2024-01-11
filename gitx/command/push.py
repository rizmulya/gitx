from settings import usernames, auth_tokens, repo_name, branch_name, default_user
import subprocess


def push(args):
    user_index = args.u if args.u is not None else default_user
    username = usernames[user_index]
    token = auth_tokens[user_index]

    branch = args.b or branch_name
    repo = args.r or repo_name

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", args.m]) 
    subprocess.run(["git", "push", "-u", f"https://{token}@github.com/{username}/{repo}.git", branch])
