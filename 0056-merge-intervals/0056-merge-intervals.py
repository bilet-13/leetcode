class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merge_list = []

        for interval in intervals:
            if not merge_list:
                merge_list.append(interval)
            
            else:
                if interval[0] <= merge_list[-1][1]:
                    merge_list[-1][1] = max(merge_list[-1][1], interval[1])
                else:
                    merge_list.append(interval)

        return merge_list
        