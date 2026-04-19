import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="common")

subparsers.add_parser("create")

guess_parser = subparsers.add_parser("guess")
guess_parser.add_argument("word")

args = parser.parse_args()

if args.command == "create":
    print("create command received")
    # Later:
    # game = wordleGame()
    # game.create_new_game()

elif args.command == "guess":
    print(f"guess command received: {args.word}")
    # later:
    # game = wordleGame()
    # game.make_guess(args.word.upper())

else:
    print("please provide either 'create' or 'guess <word>'")