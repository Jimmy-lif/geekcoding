class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordLen = 0;
        result = [];
        lines = [];
        str = [];
        for word in words:
            if wordLen + len(word) <= maxWidth:
                str.append(word);
                wordLen += len(word) + 1;
            else:
                lines.append(str);
                str = [word];
                wordLen = len(word) + 1;
        lines.append(str);
        for line in lines[:len(lines) -1]:
            wordLen = 0;
            for word in line:
                wordLen += len(word);
            blankNum = 0;
            extraNum = 0;
            if len(line) > 1:
                blankNum = int((maxWidth - wordLen) / (len(line) - 1));
                extraNum = maxWidth - blankNum * (len(line) - 1) - wordLen;
            else:
                blankNum = maxWidth - wordLen;
            outLine = '';
            for word in line[:len(line) - 1]:
                outLine += word;
                for i in range(blankNum):
                    outLine +=' ';
                if extraNum > 0:
                    outLine +=' ';
                    extraNum -= 1;
            outLine += line[len(line) - 1];
            if len(line) == 1:
                for i in range(blankNum):
                    outLine +=' ';
            result.append(outLine);

        lastline = lines[len(lines) - 1];
        outLine = '';
        for word in lastline[:len(lastline) - 1]:
            outLine += word;
            outLine += ' ';
        outLine += lastline[len(lastline) - 1];
        for i in range(maxWidth-len(outLine)):
            outLine += ' ';
        result.append(outLine);

        return result;
