class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        front = 0
        strings = ""
        for i in range (front,len(s)):
            new = ""
            end = i+1
            j = i
            while j < end and j<len(s):
                if new.find(s[j])==-1:
                    end +=1
                    new += s[j]
                    j += 1
                else:
                    end -=1
                    break
            front += 1
            if len(new)>len(strings):
                strings = new
        return len(strings)
