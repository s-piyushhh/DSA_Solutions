"""
Leetcode Problem: Find X value of Array II
Description: You are given an array of positive integers nums, and a positive integer k. You are also given a list of queries, where each query is represented as a tuple (idx, val, start, x). For each query, you need to perform the following operations:
"""


class Solution:
    def resultArray(self, nums, k, queries):
        class Node:
            __slots__ = ('prod', 'freq')

            def __init__(self):
                self.prod = 1
                self.freq = [0] * k

        n = len(nums)
        tree = [Node() for _ in range(4 * n)]

        def merge(L: Node, R: Node) -> Node:
            res = Node()
            res.prod = (L.prod * R.prod) % k
            res.freq = L.freq[:]
            for r in range(k):
                if R.freq[r]:
                    nr = (L.prod * r) % k
                    res.freq[nr] += R.freq[r]
            return res

        def build(v: int, tl: int, tr: int) -> None:
            if tl == tr:
                tree[v].prod = nums[tl] % k
                tree[v].freq[tree[v].prod] = 1
                return
            tm = (tl + tr) // 2
            build(v * 2, tl, tm)
            build(v * 2 + 1, tm + 1, tr)
            tree[v] = merge(tree[v * 2], tree[v * 2 + 1])

        def update(v: int, tl: int, tr: int, pos: int, val: int) -> None:
            if tl == tr:
                tree[v].prod = val % k
                tree[v].freq = [0] * k
                tree[v].freq[tree[v].prod] = 1
                return
            tm = (tl + tr) // 2
            if pos <= tm:
                update(v * 2, tl, tm, pos, val)
            else:
                update(v * 2 + 1, tm + 1, tr, pos, val)
            tree[v] = merge(tree[v * 2], tree[v * 2 + 1])

        def query(v: int, tl: int, tr: int, l: int, r: int) -> Node:
            if l > r:
                return Node()
            if l == tl and r == tr:
                return tree[v]
            tm = (tl + tr) // 2
            return merge(query(v * 2, tl, tm, l, min(r, tm)),
                         query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r))

        build(1, 0, n - 1)
        ans = []
        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            res = query(1, 0, n - 1, start, n - 1)
            ans.append(res.freq[x])
        return ans


if __name__ == "__main__":
    solution = Solution()
    # nums = [1, 2, 3, 4, 5]
    # k = 3
    # queries = [(0, 6, 1, 0), (2, 7, 0, 1)]
    nums = [1,2,3,4,5]
    k = 3
    queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]
    # Output: [2,2,2]
    
    print(solution.resultArray(nums, k, queries))  # Example usage