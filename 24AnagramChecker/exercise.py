def isAnagram(word1, word2):
    if len(word1) != len(word2):
        return False

    word1 = word1.lower()
    word2 = word2.lower()

    for letter in word1:
        if word1.count(letter) != word2.count(letter):
            return False

    return True

print("Enter two strings and I'll tell you if they are anagrams:")

first = input("Enter the first string: ")
second = input("Enter the second string: ")

if isAnagram(first, second):
    print('"' + first + '" and "' + second + '" are anagrams.')
else:
    print('"' + first + '" and "' + second + '" are not anagrams.')
