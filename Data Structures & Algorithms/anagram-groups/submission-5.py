class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap: key - [] of count of 26 chars, value - [] of strings
        hash = {}
        for str in strs:    # O(len(strs))
            count = [0] * 26
            for char in str:  
                index = ord(char) - ord('a')
                # add it to count
                count[index] += 1
            
            count_tuple = tuple(count)
            if count_tuple in hash:
                hash[count_tuple].append(str)
            else:
                hash[count_tuple] = [str]
        
        result = []
        for key, value in hash.items():
            result.append(value)
        
        return result
