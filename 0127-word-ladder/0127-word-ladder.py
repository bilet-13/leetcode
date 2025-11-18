class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs start from beginword
        # node: word in wordlist or beginword or endword
        # edge: node a -> node b ifnode b can be obtain by change only one letter in node a
        # if reach endWord update length(initialize 0)
        # time complexity o(V + E) = o(n + )
        # time complexity o (n * 26 * len of a word) x
        # we need ot find min word so we need to backtrack
        # backtrack so time complexity o(n^len of list)?
        # dfs may be quick

        # in bfs

        #     for i in range(word length):
        #         for char in 26 char
        #             change the word[i] to char
        words = set(wordList)
        visited = {beginWord}
        queue = deque([(beginWord, 1)])

        while queue:
            cur, cur_num_trans = queue.popleft()

            if cur == endWord:
                return cur_num_trans

            for i in range(len(cur)):
                cur_chr = cur[i]
                for j in range(26):
                    nbr = list(cur)
                    nbr[i] = chr(ord('a') + j)
                    nbr = "".join(nbr)

                    if nbr not in visited and nbr[i] != cur_chr and nbr in words:
                        visited.add(nbr)
                        queue.append((nbr, cur_num_trans + 1))
        
        return 0 
                

        
        