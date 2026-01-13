class Solution:
    def addBinary(self, a: str, b: str) -> str:

        max_len = max(len(a),len(b))

        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0
        output = ""
        for i in range(max_len):
            total = int(a[-(i+1)]) + int(b[-(i+1)]) + carry
            output = str(total%2) + output
            carry = total//2

        if carry:
            output = "1" + output

        
        return output