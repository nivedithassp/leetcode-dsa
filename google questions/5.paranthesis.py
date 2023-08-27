#https://leetcode.com/problems/valid-parentheses/submissions/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

class Solution(object):
    def isValid(self, s):
        symlist = []
        for c in s :
            if c in ['(','{','[']:
                symlist.append(c)
            elif c == ')' and len(symlist) != 0 and symlist[-1] =='(' :
                symlist.pop()
            elif c == '}' and len(symlist) != 0 and symlist[-1] =='{' :
                symlist.pop()
            elif c == ']' and len(symlist) != 0 and symlist[-1] =='[' :
                symlist.pop()
            else :
                return False
        return  symlist == []

