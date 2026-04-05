class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        #get frequencies of each char in t
        needSet = {}
        for char in t:
            needSet[char] = 1 + needSet.get(char, 0)
        need = len(needSet)

        haveSet = {}
        have = 0  
        l = 0
        res, resLen = [-1,-1], float("infinity")
        
        for r in range(len(s)):
            char = s[r]
            #fill have set with freq of each char
            haveSet[char] = 1 + haveSet.get(char, 0)

            if char in needSet and haveSet[char] == needSet[char]:
                have += 1
            
            while have == need:
                #update values
                if((r - l + 1) < resLen):
                    res = [l,r]
                    resLen = (r - l + 1)
                
                leftchar = s[l]
                haveSet[leftchar] -= 1

                if leftchar in needSet and haveSet[leftchar] < needSet[leftchar]:
                    have -= 1
                l += 1
        l,r = res
        return s[l: r + 1] if resLen != float("infinity") else ""



        