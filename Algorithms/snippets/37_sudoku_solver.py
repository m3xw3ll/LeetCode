class Solution:
    def is_empty(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '.':
                    return (i, j)

        return None

    def validation(self, grid, number, position):
        for i in range(len(grid[0])):
            if grid[position[0]][i] == str(number) and str(position[1]) != str(i):
                return False

        for i in range(len(grid)):
            if grid[i][position[1]] == str(number) and str(position[0]) != str(i):
                return False

        x_box = int(position[1]) // 3
        y_box = int(position[0]) // 3

        for i in range(y_box * 3, y_box * 3 + 3):
            for j in range(x_box * 3, x_box * 3 + 3):
                if grid[i][j] == str(number) and (i, j) != position:
                    return False

        return True

    def backtrack(self, grid):
        empty = self.is_empty(grid)
        if not empty:
            return True
        else:
            row, column = empty

        for i in range(1, 10):
            if self.validation(grid, i, (row, column)):
                grid[row][column] = str(i)

                if self.backtrack(grid):
                    return True

                grid[row][column] = '.'

        return False

    def solve_sudoku(self, board):
        self.backtrack(board)


if __name__ == '__main__':
    c = Solution()
    c.solve_sudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                          [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
