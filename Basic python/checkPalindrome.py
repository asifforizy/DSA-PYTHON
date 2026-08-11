def isPalindrome(s, l, r):
    if l >= r:
        return True

    if s[l] != s[r]:
        return False

    return isPalindrome(s, l + 1, r - 1)


s = "madam"

print(isPalindrome(s, 0, len(s) - 1))



def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


s = "madam"

print(isPalindrome(s))