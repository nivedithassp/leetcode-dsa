
class Solution:
        strs = ["flower","flow", "flight"]
        lcp = ""

        if strs is None or len(strs )== 0:
             print(lcp)
        minlength = len(strs[0])
        for i in range(1 ,len(strs)):
            minlength = min(minlength ,len(strs[i]))

        for i in range (0 ,minlength) :
            current = strs[0][i]
            for j in range (0 ,len(strs)):
                if strs[i][j ]!= current :
                    print(lcp)
            lcp += current

        print(lcp)
