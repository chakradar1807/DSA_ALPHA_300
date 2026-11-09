class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = 0
        ans = ""
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break
        for j in range(idx, -1, -1):
            ans += word[j]
        for k in range(idx + 1, len(word)):
            ans += word[k]
        return ans
