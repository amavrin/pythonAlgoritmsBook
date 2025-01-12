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


def is_palindrome4(w):
    left, right = 0, len(w) - 1
    while left < right:
        if w[left] != w[right]:
            return False
        left += 1
        right -= 1
    return True


def main():
    print(is_palindrome4("a" * 100 + "b"))


if __name__ == "__main__":
    main()