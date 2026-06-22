"""
Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student receives atleast one book.
Each student is assigned a contiguous sequence of books.
No book is assigned to more than one student.
All books must be allocated.
The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: If it is not possible to allocate books to all students, return -1.
"""


class Solution:
    def findPages(self, arr, k):
        # code here
        if len(arr) < k:
            return -1

        def helper(mid):
            currPages = 0
            stds = 1

            for i in arr:
                if i > mid:
                    return False

                if currPages + i > mid:
                    stds += 1
                    currPages = i

                    if stds > k:
                        return False
                else:
                    currPages += i

            return True

        l = max(arr)
        r = sum(arr)

        while l <= r:
            mid = l + (r - l) // 2

            if helper(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l


if __name__ == "__main__":
    obj = Solution()

    arr = [12, 34, 67, 90]
    k = 2
    
    # arr = [15, 17, 20]
    # k = 5
    
    ans = obj.findPages(arr, k)

    print(ans)
