# Computational Thinking Mini Project

## Command-line wordle API and bot

There are two components to this - the API and the bot. Both components have access to the dictionary of valid words, SOWPODS. https://github.com/jesstess/Scrabble/blob/master/scrabble/sowpods.txt

### The API

The API should give you ways to create a game of wordle (which resets the correct answer) and make a guess. It should provide appropriate responses - for instance if the correct answer is "SNAKE" and you say `python3 wordleserver guess SPEAR` it should respond with `💚🩶💛💛🩶`. Of course, if you've run out of guesses, it would say `out of guesses, please run python3 wordleserver create`.

Detailed functionality:

1. `python3 wordleserver create` -> creates a new game. Since you have to call the code again and again, consider using a text file to store the state of the game. 5 letter words are standard.
2. `python3 wordleserver guess [AWORD]` -> guesses `AWORD` as the player's next guess and gives feedback. Internally updates the game state accordingly.

### The bot

The bot should win the game, of course. It should call the API and create a game for itself, then it gets six guesses. The bot can use any strategy you want - it can pick a word at random if you want it to. PLEASE NOTE: THE BOT PLAYS THE GAME, NOT YOU! The bot gets access to the list of valid words, SOWPODS, and gets to pick any of those words. It wins or loses without any human intervention.

Detailed functionality:

1. `python3 wordlebot attempt` -> In turn calls `python3 wordleserver create` and informs the user if a game has successfully been created. Then prints a series of at most six `I am going to guess <some word>` messages followed by `I got the feedback: <feedback>`. Records its victory or failure.

### The goal

Creating a bot that performs better than picking a random word every time, and instrumenting how much better than the random bot it is. (maybe run it 100 times and see how many games each bot wins)

### Alternatively....

The server can also expose functions in such a way that the bot can `import` the server and without having to execute the script just call a function.

## Work in...

Teams of 3, decided randomly. Your team assignments await you after the break. Git is highly recommended but not currently mandated. You're going to be forced to use git very soon so if you want to get the practice in, please do.

## Due on...

16:00, 21 Apr 2026 (Tuesday).

## What is due?

A presentation including a code walkthrough.

## Should I need to include (some proprietary software generated deck)?

Choose whatever presentation aids you think will help you best communicate what work went into this.'

# This activity is scored! It will contribute upto 10 points towards your final score in this program