from __future__ import annotations

import json
from typing import TypedDict


class HistoryItem(TypedDict):
    guess: str
    feedback: str


class GameState:
    FILE_NAME = "gamestate.json"

    def __init__(
        self,
        attempts_made: int = 0,
        target_word: str = "",
        history: list[HistoryItem] | None = None,
        won: bool = False
    ):
        self.attempts_made = attempts_made
        self.target_word = target_word
        self.history = history if history is not None else []
        self.won = won
    # i could have simply used a constructor over here but use krne ke liye hame values pata honi chahiye jo ham fields me pass krenge.
    # but, idhr toh malum hii nai hai kya values present hai json file mei.. so simply read them first and then constructor use kro. Thats the idea
    # Thus, i wrote a class method which internally uses the constructor (cls).

    @classmethod
    def load(cls) -> "GameState": # what is happening here?
        with open(cls.FILE_NAME, "r") as file:
            data = json.load(file)

        return cls(
            attempts_made=data["attempts_made"],
            target_word=data["target_word"],
            history=data["history"],
            won=data["won"],
        )

    def save(self) -> None:
        data = {
            "attempts_made": self.attempts_made,
            "target_word": self.target_word,
            "history": self.history,
            "won": self.won,
        }

        with open(self.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4) # send in updated history everytime, as "w" rewrites everything present in the file.
