class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        deadends = set(deadends)

        if target in deadends or "0000" in deadends:
            return -1

        queue = deque()
        queue.append(("0000", 0))

        while queue:
            cur, step = queue.popleft()

            if cur in visited:
                continue
            visited.add(cur)

            if cur == target:
                return step

            for i in range(len(cur)):
                for d in [1, -1]:
                    neighbor = list(cur)
                    change_val = 9 if int(cur[i]) + d < 0 else (int(cur[i]) + d) % 10
                    neighbor[i] = str(change_val)
                    neighbor = "".join(neighbor)

                    if neighbor not in visited and neighbor not in deadends:
                        queue.append((neighbor, step + 1))

        return -1

        