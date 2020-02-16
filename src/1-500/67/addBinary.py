class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bnA = 0;
        for i in range(len(a)):
            bnA = bnA * 2 + int(a[i]);

        bnB = 0;
        for i in range(len(b)):
            bnB = bnB * 2 + int(b[i]);

        sumAB = bnA + bnB;
        return str(bin(sumAB))[2:];