'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    pair = 'th'
    if word:
        first, *rest = word
        if rest:
            second, *third = rest
            if first + second == pair:
                return count_th(third) + 1
            return count_th(rest)
    return 0
