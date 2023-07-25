class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                out += word1[i]
                i += 1
            if j < len(word2):
                out += word2[j]
                j += 1
        return out
        #attempt3
        # word1 = list(word1)
        # word2 = list(word2)
        # out = ""
        # while word1 or word2:
        #     if word1:
        #         out += word1.pop(0)
        #     if word2:
        #         out += word2.pop(0)
        # return out
        #attempt2
        # out = list(zip(word1,word2))
        # strout = "".join(["".join(a) for a in out])
        # if len(word1) > len(out):
        #     strout += word1[len(out):]
        # if len(word2) > len(out):
        #     strout += word2[len(out):]
        # return strout
        #attempt1
        # print(list(zip(word1,word2)))
        # overlap = min(len(word1),len(word2))
        # out = "".join([f'{word1[i]}{word2[i]}' for i in range(0,overlap)])
        # if len(word1) > overlap:
        #     out += word1[overlap:]
        # if len(word2) > overlap:
        #     out += word2[overlap:]
        # return out
