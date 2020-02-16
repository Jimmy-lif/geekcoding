class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bnA = int(a,2)
        bnB = int(b,2)
        sumAB = bnA + bnB;
        return str(bin(sumAB))[2:];