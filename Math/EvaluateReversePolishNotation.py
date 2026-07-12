"""
leetcode Problem: 150
Description: Evaluate the value of an arithmetic expression in Reverse Polish Notation.

"""

class Solution:
    def evalRPN(self, tokens):
        st = []
        for i in tokens:
            if i in {'+', '-', '*', '/'}:
                a = st.pop()
                b = st.pop()
                if i == '+':
                    st.append(a+b)
                elif i == '-':
                    st.append(b-a)
                elif i == '*':
                    st.append(a*b)
                elif i == '/':
                    st.append(int(b/a))
            else:
                st.append(int(i))
            # print(st)

        return st[-1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
    print(s.evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6