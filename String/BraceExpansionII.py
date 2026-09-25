'''
Leetcode 1096. Brace Expansion II
Description:Under the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the expression represents.

The grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the three rules for our grammar:

For every lowercase letter x, we have R(x) = {x}.
For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.'''


class Solution:
    def braceExpansionII(self, expression: str):
        idx = 0
        n = len(expression)

        def is_letter(c: str) -> bool:
            return "a" <= c <= "z"

        # Recursive descent parser
        def expr() -> set:
            nonlocal idx
            ret = set()
            while True:
                # Take the union with the result of term()
                ret |= term()
                # Continue if a comma is matched; otherwise, stop matching
                if idx < n and expression[idx] == ",":
                    idx += 1
                    continue
                else:
                    break
            return ret

        # term -> item | item term
        def term() -> set:
            nonlocal idx
            # Initialize an empty set and take its Cartesian product with subsequent results
            ret = {""}
            # An item starts with { or a lowercase letter; continue matching only when this condition is met
            while idx < n and (
                expression[idx] == "{" or is_letter(expression[idx])
            ):
                sub = item()
                tmp = set()
                for left in ret:
                    for right in sub:
                        tmp.add(left + right)
                ret = tmp
            return ret

        # item -> letter | { expr }
        def item() -> set:
            nonlocal idx
            ret = set()
            if expression[idx] == "{":
                idx += 1
                ret = expr()
            else:
                ret = {expression[idx]}
            idx += 1
            return ret

        ret = expr()
        return sorted(list(ret))

if __name__ == "__main__":
    expression = "{a,b}{c,{d,e}}"
    solution = Solution()
    result = solution.braceExpansionII(expression)
    print(result)  # Output: ['ac', 'ad', 'ae', 'bc', 'bd', 'be']