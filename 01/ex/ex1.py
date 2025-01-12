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
    return w[full:half:-1] == w[:half]


def main():
    print(is_palindrome3("abcba"))
    print(is_palindrome3("abcb"))


if __name__ == "__main__":
    main()