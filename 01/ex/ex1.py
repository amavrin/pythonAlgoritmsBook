def is_palindrome1(w):
    return w[::-1] == w


def is_palindrome2(w):
    while len(w) > 1:
        if w[0] != w[-1]:
            return False
        w = w[1:-1]
    return True


def is_palindrome3(w):
    full = len(w)
    half = full//2
    if full % 2 == 0:
        return w[full-1:half-1:-1] == w[:half]
    else:
        return w[full-1:half:-1] == w[:half]


def main():
    print(is_palindrome3("abba"))
    print(is_palindrome3("abcba"))
    print(is_palindrome3("abcb"))


if __name__ == "__main__":
    main()