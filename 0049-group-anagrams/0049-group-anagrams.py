class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) # key: tuple() 26 element represesnt the number of each char g val: array of strs
        # for each strs check it is anagram with key
        # if yes add it to array, if not create new group
        # time complexity o(n * check anagramn) = o(n * len of curr str)

        for word in strs:
            frequency = [0 for _ in range(26)]

            for char in word:
                frequency[ord(char) - ord('a')] += 1
            key = tuple(frequency)

            group[key].append(word)

        return [group[key] for key in group]
        