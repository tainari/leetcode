class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letters = ["","a","b","c","d","e","f","g","h"]
        col, row = coordinates[0],int(coordinates[1])
        if row % 2:
            if letters.index(col) % 2:
                return False
            else:
                return True
        else:
            if letters.index(col) % 2:
                return True
        return False
