class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialization
        num = ""
        digits = [0] * (max(len(num1), len(num2)))
        carry = 0

        # Balance the number of digits of two strings
        while len(num1) < len(num2):
            num1 = "0" + num1
        while len(num2) < len(num1):
            num2 = "0" + num2

        # Calculate the result
        for digit_index in range(len(num1) - 1, -1, -1):
            digit_num1 = ord(num1[digit_index]) - 48 
            digit_num2 = ord(num2[digit_index]) - 48

            digit = digit_num1 + digit_num2 + carry
            if digit < 10:
                carry = 0
            else: 
                carry = 1
                digit -= 10

            digits[digit_index] = digit

        #Check if carry = 1?
        if carry == 1:
            digits.insert(0, 1)

        #convert list to string
        for digit in digits:
            num += chr(digit + 48) # cong them 48 de tra ve dung ki tu

        # Answer 
        return num
        
