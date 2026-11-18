class Solution:
    def frequencySort(self, s: str) -> str:
        map = {}
        for i in s:
            map[i] = map.get(i,0)+1
        
        map = sorted(map.items(),key=lambda i: -i[1])

        return ''.join([key * val for key,val in map])

