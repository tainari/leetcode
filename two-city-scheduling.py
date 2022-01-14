#answer to: https://leetcode.com/problems/two-city-scheduling/submissions/
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #find number of people that should be in each city (half of total)
        n = len(costs)/2
        #create list of deltas between each cost as well as cost to city 1 and cost to city 2
        deltas = [[a[0] - a[1],a[0],a[1]] for a in costs]
        #sort by delta. 
        #this step and the previous step can be combined as sorted(costs,key = lambda x: x[0]-x[1]), but i didn't know that at the time
        deltas = sorted(deltas, key=lambda x: x[0])
        #calculate the total cost. First half goes to city 1 (either cheaper or comparatively less expensive to go to city 1)
        #second half goes to city 2
        total = sum([arr[1] if ind < n else arr[2] for ind,arr in enumerate(deltas)])
        return total
