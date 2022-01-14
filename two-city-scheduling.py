class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)/2
        deltas = [[a[0] - a[1],a[0],a[1]] for a in costs]
        deltas = sorted(deltas, key=lambda x: x[0])
        total = sum([arr[1] if ind < n else arr[2] for ind,arr in enumerate(deltas)])
        return total
