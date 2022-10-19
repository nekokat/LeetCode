"""
999. Available Captures for Rook  https://leetcode.com/problems/available-captures-for-rook/
"""

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        a = "".join(map("".join,board))
        position = a.index("R")
        rook_row, rook_col = position//8, position%8
        col = "".join(l for i in range(8) if (l:=board[i][rook_col]) != ".")
        row = "".join(i for i in board[rook_row] if i != ".")

        def countpawns(line: str) -> int:
            return line.count("pR") + line.count("Rp")

        return countpawns(col)+countpawns(row)
