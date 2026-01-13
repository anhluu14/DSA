class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Initialization
        new_digits = [0] * len(digits)
        carry = 1
        # Calculate the new digit
        for digit_index in range (len(digits) - 1, -1, -1): 
        #sau khi thuc hien for loop thi se bien thanh digit index moi do    minh for lui lai chu khong for tien len nen phai -1
        #so o giua khong the la 0 vi vong lap khi toi so 0 se dung vi khong duoc xet nen phai lui lai them 1 phan tu nua
            new_digits[digit_index] = digits[digit_index] + carry

            if new_digits[digit_index] == 10:
                new_digits[digit_index] = 0
                carry = 1
            else:
                carry = 0
        #Check if carry = 1 truong hop so 999
        if carry ==1:
            new_digits.insert(0,1)

        # Answer
        return new_digits
