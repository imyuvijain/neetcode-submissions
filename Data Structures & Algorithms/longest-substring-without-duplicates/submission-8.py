class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        L = R = maxCount = 0
        seen = set()
        
        while R < len(s):
            if s[R] not in seen:
                seen.add(s[R])
                maxCount = max(len(seen), maxCount)
                R += 1
            else:
                while L < R:
                    if s[L] != s[R]:
                        seen.remove(s[L])
                        L += 1
                        
                    else:
                        L += 1
                        R += 1
                        break
                    
        return maxCount