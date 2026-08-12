class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_d = {}
        for c in t:
            t_d[c] = t_d.get(c, 0) + 1
        required = len(t_d)
        l = 0
        formed = 0
        best_length = float('inf')
        best_start = 0
        window = {}
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in t_d and window[c] == t_d[c]:
                formed += 1
            while formed == required:
                if  r- l + 1 < best_length:
                    best_length = r - l + 1
                    best_start = l
                window[s[l]] -= 1
                if s[l] in t_d and window[s[l]] < t_d[s[l]]:
                    formed -= 1
                l += 1
        best_length = best_length if best_length != float('inf') else 0
        return s[best_start:best_start+best_length]
