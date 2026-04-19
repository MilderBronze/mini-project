import random

from game.feedback import FeedbackGenerator
from game.gamestate import GameState


class WordleGame:
    def __init__(self):
        with open("sowpods.txt", "r") as file:
            all_words = file.read().split()

        self.valid_words = [word for word in all_words if len(word) == 5]

    def create_new_game(self):
        """
            1. Load valid 5-letter words from sowpods.txt
            2. Randomly pick one
            3. Create a fresh GameState
            4. Save it
            5. Return a success message
        """
        chosen_word = random.choice(self.valid_words)

        state = GameState(
            attempts_made=0,
            target_word=chosen_word,
            history=[]
        )

        state.save()

        return {
            "success": True,
            "message": "New game created successfully"
        }

    def evaluate_guess(self, guess_word):
        """
            1. Load GameState
            2. Validate:
                - game exists
                - attempts < 6
                - word length is 5
                - word exists in dictionary :: iske liye alag se error handling implement kr skte hain :: look into this later
            3. Generate feedback using FeedbackGenerator
            4. Increment attempts
            5. Append to history
            6. Save GameState
            7. Return either feedback or an error message
        """
        gamestate = GameState.load()
        # validation
        if gamestate.attempts_made == 6:
            print("attempts exceeded")
            return {
                "success": False,
                "message": "maximum attempts exceeded. Start a new game."
            }

        if len(guess_word) != 5:
            print("word of insufficient length, try again.")
            return {
                "success": False,
                "message": "Word of insufficient length, try again."
            }

        if guess_word not in self.valid_words:
            print("word not found! Try again with a valid word.")
            return {
                "success": False,
                "message": "Word not found! Try again with a valid word."
            }
        # yaha tak aaya matlab valid hai.
        # finally evaluation kro. feedback
        feedback = FeedbackGenerator.generate_feedback(gamestate.target_word,guess_word)
        gamestate.attempts_made += 1
        gamestate.history.append({
            "guess": guess_word,
            "feedback": feedback
        })
        gamestate.save()
        return {
            "success": True,
            "feedback": feedback,
            "message": "Guess evaluated successfully"
        }