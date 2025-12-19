class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
          people.sort()
        left = 0
        right = len(people) - 1

        min_num_boat = 0

        while left <= right:
            if left == right:
                min_num_boat += 1
                break
            
            if people[right] + people[left] > limit:
                min_num_boat += 1
                right -= 1
            else:
                min_num_boat += 1
                right -= 1
                left += 1
        
        return min_num_boat

            
            
        
        