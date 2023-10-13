## About
GITX — Automate Git Tasks with A Single Command.

When using Git, we often need to input multiple commands, such as git init, git add, git commit, and so on, for tasks like creating a new repository. Updating a repository involves repetitive commands like git add, git commit, and git push, which can be boring, especially in collaborations.

GITX simplifies this process. With just one command, 'gitx,' you can create repositories, push changes, and more. It streamlines repetitive tasks, making Git usage more efficient and less tedious.

## Installation
```
$ git clone https://github.com/rizmulya/gitx.git
$ cd gitx && sudo chmod +x gitx
$ sudo mv gitx /usr/local/sbin
```

## Usage
```console
$ gitx --help

Usage: gitx <command> [arguments]
Commands:
  init [repo_url] [branch_name] - Initialize the Git repository.
  commit <message> - Stage and commit changes.
  push <message> [branch_name] - Stage, commit, and push changes.
  branch <branch_name> - Create and switch to a new branch.
  pull - Fetch and pull changes from the remote repository.
  config - Edit the configuration file.
Note: <command> is required. [arguments] are optional, defaults to config variables.
```
