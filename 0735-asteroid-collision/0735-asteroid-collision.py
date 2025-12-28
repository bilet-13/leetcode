class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
          # stack
        # 2 4 -4 -1 -> 2 -1 -> 2
        stack = []

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                while stack:
                    asteroid1 = stack.pop()
    
                    if not (asteroid1 > 0 and asteroid < 0):
                        stack.append(asteroid1)
                        stack.append(asteroid)
                        break

                    if abs(asteroid1) == abs(asteroid):
                        break

                    elif abs(asteroid1) > abs(asteroid):
                        stack.append(asteroid1)
                        break
                    else:
                        if not stack:
                            stack.append(asteroid)
                            break
                        continue
        
        return stack
                        
                        
        