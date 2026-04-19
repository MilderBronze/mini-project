## api
- game reset ho skta.
- for each guess, the bot would run python3 wordleserver guess SPEAR
    -- response: the guess would be made, eg: SNAKE -> verification happens: -> response is returned back to the user : 💚🩶💛💛🩶
    -- on each response, increment the counter, check if it exceeded 6 trials. If yes: console the following message on the screen:
    "out of guesses. Please run python3 wordleserver create to restart the game."
    -- if the bot tries guessing and it didn't exist in the wordlist, return word doesn't exist
    -- if the bot tries guessing and it tried submitting the game too early, return word too short
    -- the alphabets can repeat


## future implementation:
- we can even add support for the user to play it manually. so player class -> implemented by man, bot -- to be looked into later.
