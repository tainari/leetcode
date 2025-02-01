class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        #INITIAL APPROACH (code left commented in)
        #for each pair, check if x > the end of a thing
        #check if y < than the beginning of a sequence
        #if adding to the end of an existing sequence, 
        #check chain n+1
        #if adding to the beginning of an existing sequence,
        #check chain n-1
        #BUT! When we sort by the second item in the sequence, 
        #we guarantee starting the chain with x[0]
        #so checking for y < pair_chain[n][0] is unnecessary
        #but this also means that, since the next item has the
        #smallest possible y, it will naturally be the next in the pair
        pairs.sort(key=lambda x: x[1])
        #pair_chain = []
        last_pair = pairs[0]
        chain_length = 1
        for x,y in pairs[1:]:
            if x > last_pair[1]:
                chain_length += 1
                last_pair = [x,y]
        return chain_length
            #added = False
            # for n, p in enumerate(pair_chain):
            #     if x > p[-1]:
            #         pair_chain[n].extend([x,y])
            #         added = True
            #         if n+1 < len(pair_chain) and pair_chain[n+1][-1] > y:
            #             link = pair_chain.pop(n+1)
            #             pair_chain[n].extend(link)
                # elif y < p[0]:
                #     pair_chain[n] = [x,y] + pair_chain[n]
                #     #pair_chain[n].append([x,y])
                #     added = True
                #     if n > 0 and pair_chain[n-1][0] < x:
                #         link = pair_chain.pop(n)
                #         pair_chain[n-1].extend(link)
        #     if not added:
        #         pair_chain.append([x,y])
        # return max([len(a)//2 for a in pair_chain])
