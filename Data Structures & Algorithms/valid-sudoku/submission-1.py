class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #bitmap
        rows = [0] * 9
        cols = [0] * 9 
        squares = [0] * 9
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                #get index of bit 
                bit_index = int(board[row][col]) - 1
                #check if a number is alread there
                if (1 << bit_index) & rows[row]:
                    return False
                if (1 << bit_index) & cols[col]:
                    return False
                if (1 << bit_index) & squares[(row // 3) * 3 + (col // 3)]:
                    return False
                
        

                rows[row] = rows[row] | 1 << bit_index
                cols[col] = cols[col] | 1 << bit_index
                squares[(row // 3) * 3 + (col // 3)] |= (1 << bit_index)
        return True