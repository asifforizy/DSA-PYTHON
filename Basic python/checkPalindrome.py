def isPalindrome(s, l, r):
    if l >= r:
        return True

    if s[l] != s[r]:
        return False

    return isPalindrome(s, l + 1, r - 1)


s = "madam"

print(isPalindrome(s, 0, len(s) - 1))