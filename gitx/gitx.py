from params import param
import argparse


def main():
    parser = argparse.ArgumentParser(description='GITX —— Automate Git Tasks with A Single Command')
    subparsers = parser.add_subparsers(title='Subparser', dest='subcommand', help='Select subcommand')
    param(parser, subparsers)


if __name__ == '__main__':
    main()
