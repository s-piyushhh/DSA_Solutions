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