class FeedbackGenerator:
    @staticmethod
    def generate_feedback(target_word: str, guess_word: str) -> str:
        result = ["🩶"] * len(guess_word)

        remaining_letters = list(target_word)

        for i in range(len(guess_word)):
            if guess_word[i] == target_word[i]:
                result[i] = "💚"

                remaining_letters[i] = None

        for i in range(len(guess_word)):
            if result[i] == "💚":
                continue

            letter = guess_word[i]

            if letter in remaining_letters:
                result[i] = "💛"

                matching_index = remaining_letters.index(letter)
                remaining_letters[matching_index] = None

        return "".join(result)