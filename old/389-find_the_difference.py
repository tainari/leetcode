class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #I'm shocked that iterating with t.count(ch) > s.count(ch) is faster?
        chardict = {ch:0 for ch in t}
        for ch in s: 
            chardict[ch] += 1
        for ch in t:
            chardict[ch] -= 1
        for ch, ct in chardict.items():
            if ct == -1:
                return ch
        ## OPTION 4 - 11%
        # t = list(t)
        # for ch in s:
        #     t.pop(t.index(ch))
        # return t[0]
        ##OPTION 3 - 10%
        # s = list(s)
        # for ch in t:
        #     try:
        #         s.pop(s.index(ch))
        #     except:
        #         return ch
        # return t[-1]
        ##OPTION 2 - 14%
        # t = list(t)
        # t.sort()
        # s = list(s)
        # s.sort()
        # for n, ch in enumerate(s):
        #     if ch != t[n]:
        #         return t[n]
        # return t[-1]
        ##OPTION 1: FAILS (e.g., s='a',t='aa'
        # return list(set(t).difference(s))[0]
