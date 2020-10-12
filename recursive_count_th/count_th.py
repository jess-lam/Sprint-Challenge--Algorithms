'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    
    # TBC
    if len(word) < 2:
        return count
    elif word[0] + word[1] == 'th':
        count = count + 1
        return count + count_th(word[2: ])
    else:
        return count_th(word[1: ])
    

