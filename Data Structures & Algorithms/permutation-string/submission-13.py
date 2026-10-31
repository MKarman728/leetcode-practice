class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_l = len(s1)
        s1_d = Counter(s1)
        s2_d = Counter(s2[:s1_l])
        if s1_d == s2_d:
            return True
        for i in range(s1_l,len(s2)):
            window = i - s1_l
            c = s2[window]
            s2_d[c] -= 1
            if s2_d[c] == 0:
                del s2_d[c]
            c2 = s2[i]
            s2_d[c2] += 1
            if s1_d == s2_d:
                return True
        return False

