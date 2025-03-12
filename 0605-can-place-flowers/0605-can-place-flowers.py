class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        remain_flowers = n

        for index in range(len(flowerbed)):
            if(self.canPlant(flowerbed, index)):
                flowerbed[index] = 1
                remain_flowers -= 1

        return remain_flowers <= 0    

    def canPlant(self, flowerbed, index):
        leftCanPlant = True if index - 1 < 0 else flowerbed[index - 1] == 0
        rightCanPlant = True if index + 1 >= len(flowerbed) else flowerbed[index + 1] == 0

        return flowerbed[index] == 0 and leftCanPlant and rightCanPlant


            