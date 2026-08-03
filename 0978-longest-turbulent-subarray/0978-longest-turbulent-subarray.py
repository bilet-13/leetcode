class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # 2d graph low hight high
        # find slope is different xd
        # not ascedn and not decent
        # -,-, +, - ,+ , 0 , -, +
        if len(arr) == 1:
            return 1
        
        turbulent_arr = [0 for _ in range(len(arr) - 1)]

        for i in range(len(arr) - 1):
            if arr[i] != arr[i + 1]:
                turbulent_arr[i] = 1 if arr[i] > arr[i + 1] else -1
        print(turbulent_arr)
        
        prev = turbulent_arr[0]
        cur_turbulent = 1 if prev != 0 else 0
        max_turbulent = 1 if prev != 0 else 0

        for i in range(1, len(turbulent_arr)):
            print(max_turbulent)
            if turbulent_arr[i] == 0:
                cur_turbulent = 0
            elif turbulent_arr[i] * prev < 0:
                cur_turbulent += 1
            else:
                cur_turbulent = 1
                
            max_turbulent = max(cur_turbulent, max_turbulent)
            prev = turbulent_arr[i]

        return 1 + max_turbulent # len fo the arr


            
        