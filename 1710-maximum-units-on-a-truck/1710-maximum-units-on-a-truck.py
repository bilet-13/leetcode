class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        cur_box = 0
        max_num_units = 0

        for num_box, unit in sorted_box:
            add_box = min(truckSize - cur_box, num_box)

            cur_box += add_box
            max_num_units += unit * add_box

            if cur_box == truckSize:
                break
        
        return max_num_units
        