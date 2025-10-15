class DetectSquares:

    def __init__(self):
        # internal data stucture {x: {y: time}}
        self.column = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        # add the new point to correspond list
        x, y = point
        self.column[x][y] += 1
        
    def count(self, point: List[int]) -> int:
        # to check that if the input point on left lower, left higher, right lower, right upper
        # can form a square or not. time complexity 
        # 
        # for input point find the horialz and vertical, then diagonal 
        x, y = point

        if x not in self.column:
            return 0

        result = 0

        same_col = self.column[x]

        for c_y, c_count in same_col.items():
            length = abs(c_y - y)
            if c_y == y:
                continue

            result +=  c_count * self.column[x + length][y] * self.column[x + length][c_y]
            result +=  c_count * self.column[x - length][y] * self.column[x - length][c_y]

        return result

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)