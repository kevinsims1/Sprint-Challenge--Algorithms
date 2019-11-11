'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):	
    word_len = len(word)
    sub_len = len('th')

    if (word_len == 0 or word_len < sub_len):
        return 0

    if len(word) == 2:
        if word == 'th':
            count +=1
        return count
        
    elif (word[0: sub_len] == 'th'):
        count += 1
        return count_th(word[sub_len - 1:], count)
    else:
        return count_th(word[sub_len - 1:], count)

