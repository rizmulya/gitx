## About

GITX — Automate Git Tasks with A Single Command.

When using Git, we often need to input multiple commands, such as git init, git add, git commit, and so on, for tasks like creating a new repository. Updating a repository involves repetitive commands like git add, git commit, and git push, which can be boring, especially in collaborations.

- GITX simplifies this process. With just one command, 'gitx,' you can create repositories, push changes, and more. It streamlines repetitive tasks, making Git usage more efficient.
- GITX streamlines your Git workflow by enabling password-free push operations through configured credentials in the configuration file.
- GITX supports multiple GitHub credentials, allowing seamless execution of Git tasks across various accounts.

## Installation

- copy & run in the terminal :

```
git clone https://github.com/rizmulya/gitx.git && \
cd gitx && sudo chmod +x install.sh && \
sudo ./install.sh
```

- set up your configuration file:

```
sudo gitx edit
```

## Usage

```console
$ gitx --help

usage: gitx [-h] {init,commit,push,branch,pull,edit,config} ...

GITX —— Automate Git Tasks with A Single Command

options:
  -h, --help            show this help message and exit

Subparser:
  {init,commit,push,branch,pull,edit,config}
                        Select subcommand
    init                Initialize the Git repository.
    commit              Stage and commit changes.
    push                Stage, commit, and push changes.
    branch              Create and switch to a new branch.
    pull                Fetch and pull changes from the remote repository.
    edit                Edit the configuration file.
    config              Configure Git scope.



$ gitx push --help

usage: gitx push [-h] -m M [-u U] [-r R] [-b B]

(-u -r -b) are (optional), defaults to configuration file

options:
  -h, --help  show this help message and exit
  -m M        commit message (required)
  -u U        default user (default to 0)
  -r R        repository name
  -b B        branch name


$ and so on.
```
