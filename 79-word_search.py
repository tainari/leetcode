#https://leetcode.com/problems/word-search/submissions/1021234842/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ##method moves up, down, left, and right to check for word
        def check_word(word_ind, row, col, used=set()):
            #if the current square doesn't match the character at that index,
            #then return False
            if word[word_ind] != board[row][col]:
                return False
            #if it matches and we're at the end of the word, we found the word!
            #return true
            if word_ind == len(word) - 1:
                return True
            #look up, assuming the word hasn't been seen before
            if row > 0 and (row-1,col) not in used:
                #Note: must pass a "fresh" set into each recursion, otherwise you'll
                #exclude letters that were correct in an aborted path of the word
                #(e.g., as in below testcase, where order of looking meant you got
                # ABCESE and then got stuck in the upper right-hand corner
                #[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
                # "ABCESEEEFS" )
                test_up = check_word(word_ind + 1, row - 1, col, {*used, (row,col)})
                if test_up:
                    return True
            if row < n_rows - 1 and (row+1,col) not in used:
                test_down = check_word(word_ind + 1, row + 1, col, {*used, (row,col)})
                if test_down:
                    return True
            if col > 0 and (row,col-1) not in used:
                test_left = check_word(word_ind + 1, row, col - 1, {*used, (row,col)})
                if test_left:
                    return True
            if col < n_cols - 1 and (row,col+1) not in used:
                test_right = check_word(word_ind + 1, row, col + 1, {*used, (row,col)})
                if test_right:
                    return True
            #if you can't move anywhere anymore, return false
            return False

        n_rows = len(board)
        n_cols = len(board[0])

        found = False
        #iterate through each square; if the character in the square matches the first
        #of the word, then embark on your quest
        for row in range(n_rows):
            for col in range(n_cols):
                if board[row][col] == word[0]:
                    found = check_word(0,row,col)
                    #stop checking so you don't overwrite your success (if successful)
                    if found:
                        return True
        return False
