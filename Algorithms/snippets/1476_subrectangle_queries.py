class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rectangle = rectangle

    def update_rectangle(self, row1, col1, row2, col2, new_value):
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                self.rectangle[r][c] = new_value


    def get_value(self, row, col):
        return self.rectangle[row][col]


if __name__ == '__main__':
    s = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    print(s.get_value(0, 2))
    s.update_rectangle(0, 0, 3, 2, 5)
    print(s.get_value(0, 2))
    print(s.get_value(3, 1))
    s.update_rectangle(3, 0, 3, 2, 10)
    print(s.get_value(3, 1))
    print(s.get_value(0, 2))

