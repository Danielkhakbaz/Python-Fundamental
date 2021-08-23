word = input("Enter the word: ")


def isPalindrome(word: str) -> bool:
    return word == word[::-1]


print(isPalindrome(word))
