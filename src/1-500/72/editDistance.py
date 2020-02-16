def minDistance(word1: str, word2: str) -> int:
    #先找到word1中所有word2字符的位置
    idxWod2inWord1 = [len(word2)];
    if word1.find(word2) >= 0:
        return len(word1) - len(word2);  #只需要删减字符
    elif word2.find(word1) >= 0:
        return len(word2) - len(word1);  #只需要增加字符
    else:
        #找到所有字符的所有索引
        leftIdxs = [];
        for i in range(len(word2)):
            c = word2[i];
            idxC = word1.find(c);
            idxCs = [];
            while idxC >= 0:
                idxCs.append(idxC);
                idxC = subWord1.find(c,idxC+1);
            leftIdxs.append(idxCs);

        #找到递增的最长子串（不止一个）

        #以这个最长子串为基准计算操作步骤


