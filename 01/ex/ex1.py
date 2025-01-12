def is_palindrome1(w):
    return w[::-1] == w
def is_palindrome2(w):
    while len(w) > 1:
        if w[0] != w[-1]:
            return False
        w = w[1:-1]
    return True