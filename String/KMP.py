"""
Leetcode Problem: Implement strStr()
Description: Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""



class Solution:
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        
        def lpsCal(needle):
            lps = [0] * n
            i = 1
            l = 0

            while i < n:
                if needle[i] == needle[l]:
                    l += 1
                    lps[i] = l
                    i += 1
                
                else:
                    if l != 0:
                        l = lps[l-1]
                    else:
                        i += 1 

            return lps

        lps = lpsCal(needle)

        i = 0
        j = 0

        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == n:
                return i - j
            elif i < m and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
                
        return -1
    
if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    solution = Solution()
    result = solution.strStr(haystack, needle)
    print(result)  # Output: 2