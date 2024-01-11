from settings import usernames, auth_tokens, repo_name, branch_name
import subprocess
from datetime import datetime


def init(args):
    user_index = args.u if args.u is not None else 0
    username = usernames[user_index]
    token = auth_tokens[user_index]

    branch = args.b or branch_name
    repo = args.r or repo_name

    subprocess.run(["rm", "-rf", ".git"]) if args.reinit else None
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", dateNow()]) if args.reinit else subprocess.run(["git", "commit", "-m", dateNow()])
    subprocess.run(["git", "branch", "-M", branch])
    subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{username}/{repo}.git"])
    
    push_command = ["git", "push", "-u", f"https://{token}@github.com/{username}/{repo}.git", branch]
    push_command.extend(["-f"]) if args.reinit else None
    
    subprocess.run(push_command)


def dateNow():
    current_time = datetime.now()
    current_date = current_time.strftime('%y%m%d')
    return f"V{current_date}"
