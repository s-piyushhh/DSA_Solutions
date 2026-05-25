'''
LeetCode Problem: 20
Desc: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if len(st) != 0:
                if i == ")" and st[-1] == "(":
                    st.pop()
                elif i == "]" and st[-1] == "[":
                    st.pop()
                elif i == "}" and st[-1] == "{":
                    st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)

        if len(st) == 0:
            return True
        return False
    
if __name__ == "__main__":
    obj = Solution()

    # s = "()"
    s = "()[]{}"
    # s = "(]"
    # s = "([])"
    # s = "([)]"            
    
    ans = obj.isValid(s)
    
    if ans:
        print("Its Valid Paranthesis")
    else:    
        print("Its Not a Valid Paranthesis")