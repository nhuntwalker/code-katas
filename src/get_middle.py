"""Get the Middle Character (7 kyu).

You are going to be given a word.
Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.
"""


def get_middle(word):
    """Return the middle character(s) of a string."""
    chopped = list(word)
    if len(word) % 2 == 0:
        return chopped[len(chopped) / 2 - 1] + chopped[len(chopped) / 2]
    elif len(word) % 2 == 1:
        return chopped[len(chopped) / 2]
