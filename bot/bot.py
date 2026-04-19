import random

from game.game import WordleGame
from game.gamestate import GameState

class WordleBot:
    """
        rewrite this entire thing in accordance to the strategy design pattern. This algo just randomly picks up a word. #bekar.
    """
    def __init__(self):
        self.game = WordleGame()

    def attempt(self) -> bool:
        self.game.create_new_game()

        guessed_words = set()

        while True:
            game_state = GameState.load()

            if game_state.won:
                print("Bot won the game!")
                return True

            if game_state.attempts_made >= 6:
                print("Bot lost the game.")
                return False

            remaining_words = [
                word for word in self.game.valid_words
                if word not in guessed_words
            ]

            guess = random.choice(remaining_words)
            guessed_words.add(guess)

            print(f"I am going to guess {guess}")

            result = self.game.evaluate_guess(guess)

            if result["success"]:
                print(f"I got the feedback: {result['feedback']}")
            else:
                print(f"Something went wrong: {result['message']}")
                return False