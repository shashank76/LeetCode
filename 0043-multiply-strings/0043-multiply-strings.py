class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        l1, l2 = len(num1), len(num2)
        out = [0] * (l1 + l2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(l1):
            for j in range(l2):
                out[i+j] += int(num1[i]) * int(num2[j])
                out[i+j+1] += out[i+j] // 10
                out[i+j] = out[i+j] % 10
        out = out[::-1]
        i = 0
        while out[i]==0:
            i+=1
        return "".join(map(str,out[i:]))