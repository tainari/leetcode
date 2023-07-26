class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = {tuple(q) for q in queens}
        out = []
        kx,ky = king
        #check left
        for y in range(ky-1,-1,-1):
            if (kx,y) in queens:
                out.append([kx,y])
                break
        #check right
        for y in range(ky+1,8):
            if (kx,y) in queens:
                out.append([kx,y])
                break
        #check UP
        for x in range(kx-1,-1,-1):
            if (x,ky) in queens:
                out.append([x,ky])
                break
        #check down
        for x in range(kx+1,8):
            if (x,ky) in queens:
                out.append([x,ky])
                break
        #check diag_nw
        for n in range(1,min(kx,ky)+1):
            if (kx-n,ky-n) in queens:
                out.append([kx-n,ky-n])
                break
        #check diag_ne
        for n in range(1,min(kx,8-ky)+1):
            if (kx-n,ky+n) in queens:
                out.append([kx-n,ky+n])
                break
        #check diag_sw
        for n in range(1,min(8-kx,ky)+1):
            if (kx+n,ky-n) in queens:
                out.append([kx+n,ky-n])
                break
        #check diag_se
        for n in range(1,min(8-kx,8-ky)+1):
            if (kx+n,ky+n) in queens:
                print('ok')
                out.append([kx+n,ky+n])
                break
        #return 
        return out
