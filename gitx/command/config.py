from settings import usernames, emails, default_user
import subprocess


def config(args):
    if args.l or args.g:
        user_index = args.u if args.u is not None else default_user
        username = usernames[user_index]
        email = emails[user_index]
        scope = "--global" if args.g else "--local"

        subprocess.run(["git", "config", scope, "user.name", username])
        subprocess.run(["git", "config", scope, "user.email", email])
    else:
        print("error: the following arguments are required: -l or -g")
        