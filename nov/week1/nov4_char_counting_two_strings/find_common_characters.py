class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if not words:
            return []
            
        min_freq = [0] * 26
        for ch in words[0]:
            min_freq[ord(ch) - ord('a')] += 1
            
        for i in range(1, len(words)):
            curr_freq = [0] * 26
            for ch in words[i]:
                curr_freq[ord(ch) - ord('a')] += 1
                
            for j in range(26):
                if curr_freq[j] < min_freq[j]:
                    min_freq[j] = curr_freq[j]
                    
        total_chars = 0
        for count in min_freq:
            total_chars += count
            
        res = ["" for _ in range(total_chars)]
        idx = 0
        
        for j in range(26):
            for _ in range(min_freq[j]):
                res[idx] = chr(ord('a') + j)
                idx += 1
                
        return res
