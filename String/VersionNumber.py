"""
Leetcode Problem 165: Compare Version Numbers
Description:
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.

"""



class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        n1 = len(v1)
        n2 = len(v2)

        l = n1
        if n1 >= n2: l = n2

        for i in range(l):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1

        if n1 > n2:
            for i in v1[n2:]:
                if int(i) > 0:
                    return 1
        elif n2> n1:
            for i in v2[n1:]:
                if int(i) > 0:
                    return -1
        
        return 0
    

if __name__ == "__main__":
    version1 = "1.0.1"
    version2 = "1"
    solution = Solution()
    result = solution.compareVersion(version1, version2)
    print(result)  # Output: 1