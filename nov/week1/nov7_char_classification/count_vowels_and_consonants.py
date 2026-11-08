class Solution:
    def checkString(self, s: str) -> int:
        vowels = 0
        consonants = 0

        vowel_set = {'a', 'e', 'i', 'o', 'u'}

        for ch in s:
            if ch in vowel_set:
                vowels += 1
            else:
                consonants += 1

        if vowels > consonants:
            return 1
        elif vowels < consonants:
            return -1
        else:
            return 0
