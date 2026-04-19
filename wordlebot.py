import argparse

from bot.bot import WordleBot

parsers = argparse.ArgumentParser()

subparsers = parsers.add_subparsers(dest="command")

subparsers.add_parser("attempt")

args = parsers.parse_args()

if args.command == "attempt":
    bot = WordleBot()
    bot.attempt()
else:
    print("please provide the command : 'attempt'.")
