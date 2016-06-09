import re
import itertools

# e.g. 'SEND + MORE == MONEY'
def solve(puzzle):
    # find all the letters (A–Z) in the puzzle, 'SEND + MORE == MONEY')
    words = re.findall('[A-Z]+', puzzle.upper())
    # {'S','E','N','D','M','O','R','Y'}
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'

    # {'M', 'S'}
    first_letters = {word[0] for word in words}

    # n = 2
    n = len(first_letters)

    # 'SMYNEORD'
    sorted_characters = ''.join(first_letters) +\
        ''.join(unique_characters - first_letters)

    # (83, 77, 89, 78, 69, 79, 82, 68)
    characters = tuple(ord(c) for c in sorted_characters)
    # (48, 49, 50, 51, 52, 53, 54, 55, 56, 57)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]

    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation

if __name__ == '__main__':
    import sys

    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)

'''
You should now be familiar with the following techniques:
• ^ matches the beginning of a string.
• $ matches the end of a string.
• \b matches a word boundary.
• \d matches any numeric digit.
• \D matches any non-numeric character.
• x? matches an optional x character (in other words, it matches an x zero or one times).
• x* matches x zero or more times.
• x+ matches x one or more times.
• x{n,m} matches an x character at least n times, but not more than m times.
• (a|b|c) matches exactly one of a, b or c.
• (x) in general is a remembered group. You can get the value of what matched by using the groups() method
of the object returned by re.search.
'''
