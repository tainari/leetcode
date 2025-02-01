class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l = len(s)
        out = []
        m = l % k
        out = [s[n:n+k] for n in range(0,l-m,k)]
        if m:
            out.append(s[-m:] + fill*(k-m))
        return out
