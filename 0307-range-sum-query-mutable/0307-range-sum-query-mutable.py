# ==========================================
# 第一步：把我們剛剛寫好的模板，原封不動貼在最上面
# ==========================================
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2
        self._build(data, left, start, mid)
        self._build(data, right, mid + 1, end)
        self.tree[node] = self.tree[left] + self.tree[right] # 求和

    def update(self, idx, val):
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2
        if idx <= mid:
            self._update(left, start, mid, idx, val)
        else:
            self._update(right, mid + 1, end, idx, val)
        self.tree[node] = self.tree[left] + self.tree[right] # 求和

    def query(self, L, R):
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        if R < start or L > end:
            return 0 # 求和的無效值是 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2
        return self._query(left, start, mid, L, R) + self._query(right, mid + 1, end, L, R) # 求和


# ==========================================
# 第二步：填寫 LeetCode 給你的 class NumArray
# 這裡只要負責「呼叫」上面的線段樹就好
# ==========================================
class NumArray:

    def __init__(self, nums: List[int]):
        # 在這裡建立線段樹實例
        self.st = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        # 直接呼叫模板的 update
        self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        # 直接呼叫模板的 query
        return self.st.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)