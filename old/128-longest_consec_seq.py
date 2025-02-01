class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #if the list is len 0, return 0
        if not nums:
            return 0
        #find all unique numbers in list
        #can also do this with just using the list as-is and
        #keeping track of which numbers have already been seen
        uniqueNums = list(set(nums))
        #workaround for last example: if the full list is just one
        #long-ass sequence, return the length of the sequence
        if max(uniqueNums)-min(uniqueNums) == len(uniqueNums) - 1:
            return len(uniqueNums)
        #if not, we begin!
        #create a dictionary. each sequence will be represented by 
        #two keys: its highest value and its lowest value
        seqs = {}
        #here's a function that concatenates two sequences
        #if the current number N is between the start of one seq
        #and the end of the other
        def concatSeq(oldEnd,newVal,oldStart):
            #join two sequences, one ending with oldEnd
            #and one starting with oldStart, with newVal
            seq = [*seqs.pop(oldEnd),newVal,*seqs.pop(oldStart)]
            seqs[min(seq)] = seq
            seqs[max(seq)] = seq
        #here's another function that appends the number 
        #to an existing sequence
        def appendToSeq(newVal,oldVal):
            if newVal < oldVal:
                #print(seqs[oldVal])
                seq = [newVal,*seqs.pop(oldVal)]
                #print(seq)
                #seq.insert(0,newVal)
                seqs[newVal] = seq
                seqs[max(seq)] = seq
            else:
                seq = seqs.pop(oldVal)
                seq.append(newVal)
                seqs[newVal] = seq
                seqs[min(seq)] = seq
        #now, iterate through all the numbers.
        for n in uniqueNums:
            pushNum, unshiftNum = False, False
            #check if you can attach it to any existing sequence
            if n-1 in seqs:
                pushNum = True
            if n+1 in seqs:
                unshiftNum = True
            #if you can attach to both ends, combine two sequences
            if pushNum and unshiftNum:
                concatSeq(n-1,n,n+1)
            #otherwise attach it to one end or another if you can
            elif pushNum:
                appendToSeq(n,n-1)
            elif unshiftNum:
                appendToSeq(n,n+1)
            #otherwise start a new sequence
            else:
                seqs[n] = [n]
        return max([len(a) for a in seqs.values()])
