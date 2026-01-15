class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        count = 0
        n = len(chars)

        while read < n:
            count = 0
            char = chars[read]

            while read < n and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1


        return write

        
