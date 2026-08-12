class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        target_d = {}
        for c in t:
            target_d[c] = target_d.get(c, 0) + 1
        l = 0
        best_length = float('inf')
        l_start = 0
        window = {}
        match = len(target_d)
        formed = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if  c in target_d and target_d[c] == window[c]:
                formed += 1
            while formed == match:
                curr_length = r - l + 1
                if curr_length < best_length:
                    l_start = l
                    best_length = curr_length
                window[s[l]] -= 1
                if s[l] in target_d and target_d[s[l]] > window[s[l]]:
                    formed -= 1
                l += 1
        if best_length == float('inf'):
            return ""
        return s[l_start:l_start+best_length]