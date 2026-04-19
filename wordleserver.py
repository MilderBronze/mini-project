import argparse

from game.game import WordleGame

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="common")

subparsers.add_parser("create")

guess_parser = subparsers.add_parser("guess")
guess_parser.add_argument("word")

args = parser.parse_args()

game = WordleGame()

if args.command == "create":
    result = game.create_new_game()
    print("create command received")
    # Later:
    # game = wordleGame()
    # game.create_new_game()

elif args.command == "guess":
    result = game.evaluate_guess(args.word)
    if result["success"]:
        print(result["feedback"])
    else:
        print(result["message"])
    print(f"guess command received: {args.word}")
    # later:
    # game = wordleGame()
    # game.make_guess(args.word.upper())

else:
    print("please provide either 'create' or 'guess <word>'")