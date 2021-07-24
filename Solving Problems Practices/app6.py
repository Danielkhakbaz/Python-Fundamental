word = input("Enter the word: ")


def isPalindrome(word):
    return word == word[::-1]


print(isPalindrome(word))
