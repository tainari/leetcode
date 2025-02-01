class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
		#find set of all subsets of length k in s
        all_k = set()
        for i in range(len(s)-k+1):
            all_k.add(s[i:i+k])
        #if all binary codes are represented,
		#then there will be 2^k codes
        return len(all_k) == 2**k
		##FIRST ATTEMPT: deeply inefficient
		# #identify all possible binary combinations:
        # combs = ["0","1"]
        # while len(combs[0]) < k:
        #     hold = []
        #     for i in combs:
        #         hold.append(i+"0")
        #         hold.append(i+"1")
        #     combs = hold
		# # then check that each one exists in s (very expensive)
        # return all([c in s for c in combs])
