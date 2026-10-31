class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d = Counter(s1)
        s2_d = {s2[0]: 1}
        if s1_d == s2_d:
            return True
        l,r = 0, 0
        while r < len(s2) - 1:
            r += 1
            s2_d[s2[r]] = s2_d.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                c = s2[l]
                if s2_d[c] > 1:
                    s2_d[c] -= 1
                else:
                    del s2_d[c]
                l += 1
            if s1_d == s2_d:
                return True 
        return False