from command.init import init
from command.commit import commit
from command.push import push
from command.branch import branch
from command.edit import edit
from command.pull import pull
from command.config import config


def param(parser, subparsers):
    # init
    init_parser = subparsers.add_parser('init', help='Initialize the Git repository.', description='(-u -r -b -reinit) are (optional), defaults to configuration file')
    init_parser.add_argument('-m', help='commit message (required)', required=True)
    init_parser.add_argument('-u', type=int, help='default_user (default to 0)', required=False)
    init_parser.add_argument('-r', help='repository name', required=False)
    init_parser.add_argument('-b', help='branch name', required=False)
    init_parser.add_argument('-reinit', action='store_true', help='reinit git', required=False)
    # commit
    commit_parser = subparsers.add_parser('commit', help='Stage and commit changes.')
    commit_parser.add_argument('-m', help='commit message', required=True)
    # push 
    push_parser = subparsers.add_parser('push', help='Stage, commit, and push changes.', description='(-u -r -b) are (optional), defaults to configuration file')
    push_parser.add_argument('-m', help='commit message (required)', required=True)
    push_parser.add_argument('-u', type=int, help='default_user (default to 0)', required=False)
    push_parser.add_argument('-r', help='repository name', required=False)
    push_parser.add_argument('-b', help='branch name', required=False)
    # branch
    branch_parser = subparsers.add_parser('branch', help='Create and switch to a new branch.')
    branch_parser.add_argument('-b', help='branch name (required)', required=True)
    # pull
    subparsers.add_parser('pull', help='Fetch and pull changes from the remote repository.')
    # edit
    subparsers.add_parser('edit', help='Edit the configuration file.')
    # config
    config_parser = subparsers.add_parser('config', help='Configure Git scope.', description='(-u) are (optional), defaults to configuration file')
    config_parser.add_argument('-l', action='store_true', help='for --local scope', required=False)
    config_parser.add_argument('-g', action='store_true', help='for --global scope', required=False) 
    config_parser.add_argument('-u', type=int, help='default_user (default to 0)', required=False)

    args = parser.parse_args()

    commands = {
        'init': init,
        'commit': commit,
        'push': push,
        'branch': branch,
        'pull': pull,
        'edit': edit,
        'config': config,
    }
    commands.get(args.subcommand)(args) if commands.get(args.subcommand) else parser.print_help()
