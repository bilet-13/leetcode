class Solution:
    def decodeString(self, s: str) -> str:
        # bracket -> pair -> stack
        # push elemet into stack
        # when encounter the "]"
        # pop elemtn untile "[" k show up and then make the str 
        # inside [] times k and then push back to stack 
        
        stack = []

        for char in s:
            if char == ']':
                encode_chars = []

                while stack and stack[-1] != '[':
                    x = stack.pop()
                    encode_chars.append(x)
                encode_chars.reverse()
                
                stack.pop() # pop '['

                digits = []
                while stack and stack[-1].isdigit():
                    x = stack.pop()
                    digits.append(x)
                digits.reverse()
                
                k = int("".join(digits))
                
                encode_str = "".join(encode_chars) 
                decode_str = encode_str * k

                for decode_char in decode_str:
                    stack.append(decode_char)
                
            else:
                stack.append(char)
        
        return "".join(stack)
        